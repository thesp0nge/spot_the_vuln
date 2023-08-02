app.get('/user/:id', (req, res) => {
  const userId = req.params.id;
  const userData = db.users.find({ id: userId });
  res.send(userData);
});
