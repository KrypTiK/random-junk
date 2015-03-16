<?php
/*

Made by KrypTiK

You must have the following config:

$config = array();
$config['db'] = '';
$config['user'] = '';
$config['pass'] = '';
$config['host'] = 'localhost';
$config['port'] = 3306;
*/

/*
These config options are just that, options. You do not have to use them!

$config['encoding'] = 'utf8';

$con = new Simple_PDO($config);

*/

/*
To switch fetch mdoes use
$con->fetchMode();

Leave blank to reset to both
0 = Num
1 = Assoc
*/

/*

For regular queries you will use the following:

$con->query('SELECT * FROM `users');
print_r($con->getData());

or for a specific column:

print_r($con->getData('COLUMN'));
*/

/*
For prepare statements you will use the following:

$params = array(':user'=>'username');
$con->prepare('SELECT * FROM `users`',$params);

or you can select a specific column to be returned:

$con->prepare('SELECT * FROM `users`',$params,'COLUMN');

*/

class Simple_PDO {

	public function __construct($config) {

		if(isset($config['encoding'])){
			$encoding = $config['encoding'];
		} else {
			$encoding = 'utf8';
		}

		try {
			$this->dbh = new PDO("mysql:charset=".$encoding.";dbname=".$config['db'].";host=".$config['host'].";port=".$config['port'],$config['user'],$config['pass']);
			$this->dbh->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_BOTH);
		} catch (PDOException $e){
			printf("SQL Error: %s",$e->getMessage());
			exit;
		}

	}

	public function fetchMode($type){

		switch($type) {

			case "0":
				$this->dbh->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_NUM);
				break;
			case "1":
				$this->dbh->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
				break;
			default:
				$this->dbh->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_BOTH);

		}

	}

	public function query($str){

		try {
			$this->result = $this->dbh->query($str);
		} catch (PDOException $e){
			printf("SQL Error: %s",$e->getMessage());
			exit;
		}

	}

	public function prepare($str,$params,$return_column = NULL) {
		
		$this->stmt = $this->dbh->prepare($str);

		foreach($params as $param){

			if(is_int($param)){
				$this->stmt->bindParam(array_search($param, $params),$param,PDO::PARAM_INT);
			} else {
				$this->stmt->bindParam(array_search($param, $params),$param);
			}

		}

		try {
			$this->stmt->execute();
		} catch (PDOException $e){
			printf("SQL Error: %s",$e->getMessage());
			exit;
		}

		$data = array();

		if($return_column == NULL){

			while($row = $this->stmt->fetchAll()){
				$data[] = $row;
			}

		} else {

			foreach($this->stmt->fetchAll() as $row){
				$data[] = $row[$return_column];
			}

		}


		$this->stmt->closeCursor();

		return $data;

	}

	public function getData($column = NULL){

		$data = array();

		if($column == NULL){

			while($row = $this->result->fetchAll()){
				$data[] = $row;
			}

		} else {
			
			foreach($this->result->fetchAll(PDO::FETCH_ASSOC) as $row){
				$data[] = $row[$column];
			}

		}

		return $data;

	}

	public function __destruct(){

		$this->dbh = null;
	
	}

}
