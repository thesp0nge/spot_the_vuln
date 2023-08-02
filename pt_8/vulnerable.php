<?php
// Prendiamo l'input dell'utente
$username = $_POST['username'];
$password = $_POST['password'];

// Query per verificare le credenziali dell'utente
$query = "SELECT * FROM users WHERE username = '" . $username . "' AND password = '" . $password . "'";
$result = mysqli_query($connection, $query);
$row = mysqli_fetch_assoc($result);
?>
