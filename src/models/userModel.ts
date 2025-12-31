import mongoose from "mongoose";
import { IUser } from "../types/types";

const educationSchema = new mongoose.Schema(
  {
    institution: {
      type: String,
      required: true,
    },
    degree: {
      type: String,
      required: true,
    },
    startYear: {
      type: String,
      required: true,
    },
    endYear: {
      type: String,
      required: true,
    },
    results: {
      type: String,
      required: true,
    },
  },
  { _id: false }
);

const userSchema = new mongoose.Schema<IUser>(
  {
    fullName: {
      type: String,
      required: true,
    },
    shortname: {
      type: String,
      required: true,
    },
    email: {
      type: String,
      required: true,
      lowercase: true,
      match: [/^\S+@\S+\.\S+$/, "Invalid email"],
    },
    password: {
      type: String,
      required: true,
      select: false,
    },
    about: {
      type: String,
      required: true,
    },
    age: {
      type: Number,
      required: true,
    },
    address: {
      type: String,
      required: true,
    },
    languages: {
      type: [String],
      required: true,
    },
    phone: {
      type: Number,
      required: true,
    },
    jobTitle: {
      type: String,
      required: true,
    },
    education: {
      type: [educationSchema],
      required: true,
    },
  },
  { timestamps: true }
);

const User = mongoose.model<IUser>("User", userSchema);

export default User;

/* 
fullName:string,
shortName:string
email : string
password: string
about : string
age : number
address : string
Languages : string[]
linkedIn : string
links: [github : string, facebook: string, twitter: string, youtube: string]
phone : string
jobTitle : string
education : [{institution: string, degree: string, startYear: string, endYear: string, results: string}]
*/
