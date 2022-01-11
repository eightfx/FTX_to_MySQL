use crate::schema::*;

#[derive(Clone, Queryable)]
pub struct save_data_list {
    pub id: i32,
    pub exchange_name: String,
    pub symbol_name: String,
    pub table_name: String,
}
