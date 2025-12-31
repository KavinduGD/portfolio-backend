import { Document } from "mongoose";

export interface IUser extends Document {
  fullName: string;
  shortname: string;
  email: string;
  password: string;
  about: string;
  age: number;
  address: string;
  languages: string[];
  phone: number;
  jobTitle: string;
  education: {
    institution: string;
    degree: string;
    startYear: string;
    endYear: string;
    results: string;
  }[];
}
