import express, { Request, Response } from "express";

const app = express();
const port = 3000;

app.get("/", (req: Request, res: Response) => {
  res.send("Hello, TypeScript + Express!12345678");
});

app.listen(port, () => {
  console.log(`Backend server is running on http://localhost:${port}`);
});
