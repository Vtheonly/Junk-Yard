<?php
$name = $_POST['name']; // get the name from the form submission
$email = $_POST['email']; // get the email from the form submission
$message = $_POST['message']; // get the message from the form submission

$data = array(
  'name' => $name,
  'email' => $email,
  'message' => $message
); // create an array with the form data

$json = json_encode($data); // convert the array to a JSON string

file_put_contents('data.json', $json . PHP_EOL, FILE_APPEND);

?>