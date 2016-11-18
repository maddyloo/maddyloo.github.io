<!DOCTYPE html>
<html>

<body>
Choose Your Favorite Color: <br>
<script type='text/javascript' src='http://localhost/javascripts/api/viz_v1.js'></script><div class='tableauPlaceholder' style='width: 300px; height: 500px;'><object class='tableauViz' width='600' height='500' style='display:none;'><param name='host_url' value='http%3A%2F%2Flocalhost%2F' /> <param name='site_root' value='' /><param name='name' value='LiveUpdate&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='no' /><param name='showShareOptions' value='true' /><param name='refresh' value='yes'/></object></div>

<form method="post" action="index.php">
<?php
	$servername = "localhost:3306";
	$username = "Madeleine";
	$password = "password";
	$database = "madeleine";

	//create connection
	$conn = mysqli_connect($servername,$username,$password, $database)
		or die( "Unable to select database");

	$query = "SELECT * FROM colors";
	$result = mysqli_query($conn, $query);

	echo '<select id="chose_color" name="chose_color">';

	while ($row = $result->fetch_assoc()) {
		echo '<option value="'.$row['Color'].'">'.$row['Color'].'</option>';
	};

	echo '</select>';
?>


	<input type="submit" name="submit" value="Submit">
</form>

<?php
	$colors = array($result);

	if (isset($_POST['submit']) and !empty($_POST['chose_color'])) {
		// $selected_key = $_POST['chose_color'];
		// $selected_val = $colors[$_POST['chose_color']];
		$color = $_POST['chose_color'];
		$query = "UPDATE colors SET Votes = Votes + 1 WHERE color = '".$color."'";
		mysqli_query($conn,$query);	
		header("Refresh:0");
	};
?>

</body>

</html>