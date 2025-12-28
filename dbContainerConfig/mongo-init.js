const portfolioDb = process.env.PORTFOLIO_DB;
const portfolioUser = process.env.PORTFOLIO_USER;
const portfolioPassword = process.env.PORTFOLIO_PASSWORD;

db = db.getSiblingDB(portfolioDb);

db.createUser({
  user: portfolioUser,
  pwd: portfolioPassword,
  roles: [
    {
      role: "readWrite",
      db: portfolioDb,
    },
  ],
});
