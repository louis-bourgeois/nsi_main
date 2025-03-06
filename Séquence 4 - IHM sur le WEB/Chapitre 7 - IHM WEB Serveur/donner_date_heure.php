<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Donner Date & Heure</title>
    </head>
    <body>
        <h1>Ma première page PHP !!</h1>
        <p>
            <?php
            $date = date("d-m-Y");
            $heure = date("H:i");
            echo "Aujourd'hui, nous sommes le $date <br>";
            echo "et il est $heure";
            ?>
        </p>
    </body>
</html>