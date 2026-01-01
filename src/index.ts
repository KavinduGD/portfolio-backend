import express, { Request, Response } from "express";
import cors from "cors";
import morgan from "morgan";
import userRoutes from "./routes/userRoutes";
import errorHandler from "./middleware/errorMiddleware";
import connectDB from "./config/db";

const app = express();

if (process.env.NODE_ENV === "development") {
  app.use(morgan("dev"));
}
app.use(cors());
app.use(express.json());

const port = process.env.PORT || 3000;

app.use("/api/user", userRoutes);

app.use(errorHandler);

connectDB().then(() => {
  app.listen(port, () => {
    console.log(`Backend server is running on http://localhost:${port}`);
  });
});


