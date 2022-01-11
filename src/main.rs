#[macro_use]
extern crate diesel;
mod ftx;
mod lib;
pub mod schema;

use chrono::{DateTime, Local};
use diesel::mysql::MysqlConnection;
use diesel::prelude::*;
use diesel::sql_query;
use dotenv::dotenv;
use ftx::options::Options;
use ftx::ws::Result;
use ftx::ws::{Channel, Data, Orderbook, Ws};
use futures::future;
use futures::stream::StreamExt;
use std::io;
use std::io::Write;
use std::time::Duration;
use tokio::time::sleep;

#[derive(Queryable)]
struct TableSaveDataList {
    id: i32,
    exchange_name: String,
    symbol_name: String,
    table_name: String,
}
async fn loop_connect(sql_symbol: String, sql_table: String, count: u64) {
    loop {
        sleep(Duration::from_millis(5_000 * &count)).await;
        println!("{} RECONNECTING NOW!!!", &sql_symbol);
        get_ftx_data(&sql_symbol, &sql_table)
            .await
            .unwrap_or_else(|err| eprintln!("IO Error => {}", err));
    }
}
async fn get_ftx_data(sql_symbol: &String, sql_table: &String) -> Result<()> {
    dotenv().ok();

    let connection: MysqlConnection = lib::establish_connection();
    let mut websocket = Ws::connect(Options::from_env()).await?;

    let market = sql_symbol;
    let mut orderbook = Orderbook::new(market.to_owned());

    websocket
        .subscribe(vec![
            Channel::Trades(market.to_owned()),
            Channel::Orderbook(market.to_owned()),
        ])
        .await?;

    loop {
        let data = websocket.next().await.expect("No data received")?;

        let dt: DateTime<Local> = Local::now();
        let timestamp: i32 = dt.timestamp() as i32;

        match data {
            (_, Data::Trade(trade)) => {
                let sql_sentence = format!(
                "INSERT INTO {} (timestamp, price, amount, direction) VALUES ({}, {}, {}, '{:?}');",
                &sql_table,timestamp, trade.price, trade.size, trade.side,
            );

                sql_query(sql_sentence).execute(&connection).unwrap();
            }
            (_, Data::OrderbookData(orderbook_data)) => {
                orderbook.update(&orderbook_data);
                io::stdout().flush().unwrap(); // Emits the output immediately
            }
            _ => panic!("Unexpected data type"),
        }
    }
}

#[tokio::main]
async fn main() {
    use self::schema::save_data_list::dsl::*;

    let connection = lib::establish_connection();
    let results = save_data_list
        .filter(exchange_name.eq("FTX"))
        .load::<TableSaveDataList>(&connection)
        .expect("Error loading posts");

    let mut tasks = Vec::new();

    for data in results {
        let sql_symbol = std::string::String::from(&data.symbol_name);
        let sql_table = std::string::String::from(&data.table_name);
        let count = data.id as u64;

        let x = tokio::spawn(loop_connect(sql_symbol, sql_table, count));
        tasks.push(x);
    }

    let x = future::join_all(tasks.into_iter()).await;
}
