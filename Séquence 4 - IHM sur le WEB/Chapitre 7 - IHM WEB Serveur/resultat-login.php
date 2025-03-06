<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultat du login</title>
</head>
<body>
    <?php
        $name = $_POST["name"];
        $fname = $_POST["firstname"]
        $age = $_POST["age"]
        $fname = $_POST["firstname"]
        $login = $_POST["login"];
        $password = $_POST["password"];
        echo "<h2>Bonjour $nom, ton  login est : $login et ton mot de passe est $password </h2> <br>";
   
   ?>
</body>
</html>