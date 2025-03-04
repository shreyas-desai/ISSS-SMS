const serverUrl = "mongodb://localhost:27017/";
const database = "isss-login-data";

let _connection = undefined;
let _db = undefined;

if (!_connection) {
  _connection = await MongoClient.connect(serverUrl);
  _db = _connection.db(database);
}

const getCollectionFn = (collection) => {
  let _col = undefined;

  return async () => {
    if (!_col) {
      const db = await _db();
      _col = await db.collection(collection);
    }
    return _col;
  };
};
export const isssData = getCollectionFn("isss-data");
