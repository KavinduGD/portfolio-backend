import mongoose from "mongoose";

const connectDB = async () => {
  try {
    await mongoose.connect(
      `mongodb://${process.env.PORTFOLIO_USER}:${process.env.PORTFOLIO_PASSWORD}@${process.env.MONGODB_HOST}:27017/${process.env.PORTFOLIO_DB}`,
    );
    console.log("Connected to database");
  } catch (error) {
    console.log(error);
    process.exit(1);
  }
};

export default connectDB;
