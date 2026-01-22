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

export interface IAdmin extends Document {
  email: string;
  password: string;
}

export interface ITechnology extends Document {
  technology: string;
  level: number;
  icon: string;
  type: string;
}

export interface ISkill extends Document {
  skill: string;
  skillImage: string;
  description: String;
}

export interface ICertificate extends Document {
  name: string;
  issuer: string;
  issueDate: string;
  certificateImage: string;
  credentialsId: string;
  certificateLink: string;
  tags: string[];
  score: number;
}

export interface IProject extends Document {
  projectName: string;
  projectDescription: string;
  startedDate: string;
  technologies: string;
  projectImages: string[];
  links: {
    linkName: string;
    link: string;
  };

  architectureImages: {
    diagramName: string;
    imageName: string;
  }[];

  architectureDescription: string;
  tags: string[];
  score: number;
}
