import express, { Request, Response } from "express";
import cors from "cors";
import morgan from "morgan";
import userRoutes from "./routes/userRoutes";
import adminRoutes from "./routes/adminRoutes";
import technologyRoutes from "./routes/technologyRoutes";
import skillRoutes from "./routes/skillRoues";
import certificateRoutes from "./routes/certificateRoutes";
import projectRoutes from "./routes/projectRoutes";
import errorHandler from "./middleware/errorMiddleware";
import connectDB from "./config/db";
import seedAdmin from "./config/seedAdmin";
import cookieParser from "cookie-parser";
import path from "path";

const app = express();

if (process.env.NODE_ENV === "development") {
  app.use(morgan("dev"));
}
app.use(cors());
app.use(express.json());
app.use(cookieParser());

app.use("/uploads", express.static(path.join(process.cwd(), "uploads")));

const port = process.env.PORT || 3000;

app.use("/api/user", userRoutes);
app.use("/api/admin", adminRoutes);
app.use("/api/technology", technologyRoutes);
app.use("/api/skill", skillRoutes);
app.use("/api/certificate", certificateRoutes);
app.use("/api/project", projectRoutes);

app.get("/", (req: Request, res: Response) => {
  res.status(200).json({
    status: "OK",
    service: "Backend API",
  });
});

// Error Handling Middleware
app.use(errorHandler);

connectDB().then(async () => {
  await seedAdmin();
  app.listen(port, () => {
    console.log(`Backend server is running on http://localhost:${port}`);
  });
});
