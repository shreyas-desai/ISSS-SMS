import insertRoute from "./insert.js";
import cors from "cors";

const constructorMethod = (app) => {
  app.use(
    cors({
      origin: "*",
    })
  );
  app.use("/insert", insertRoute);

  app.use("*", (req, res) => {
    return res.status(404).json({ error: "Not found" });
  });
};

export default constructorMethod;
