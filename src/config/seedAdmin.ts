import Admin from "../models/adminModel";

const seedAdmin = async () => {
  // first time
  const admin = await Admin.findOne();

  if (!admin) {
    const email = process.env.ADMIN_EMAIL;
    const password = process.env.ADMIN_PASSWORD;
    console.log(email, password);

    if (!email || !password) {
      throw new Error("For the first start Admin email, password required");
    }
    const admin = new Admin({ email, password });
    await admin.save();

    console.log("Admin created in the database");
  }
};

export default seedAdmin;
