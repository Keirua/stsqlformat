# format_sql

This small piece of code adds the possibility to format SQL queries in sublime text 3 through a new command 'format_sql'. It takes some poorly formatted SQL code like this :

	select * from STuff s where s.something > 42 limit 30

and turns it into this :

	SELECT *
	FROM stuff s
	WHERE s.something > 42 LIMIT 30

Yep, I know, that's pretty awesome. Well, I'm not so sure about that, but anyway, that's really useful to me, and it may be to you to.

## Installation

Clone this repository inside of the Packages/User repository, then map the new command to a key binding

## Usage

Create the following binding in Preference / Key Bindings - User
	
	{ "keys": ["ctrl+alt+f"], "command": "format_sql" }

## External lib

I cloned the code for sqlparse from https://github.com/andialbrecht/sqlparse into the project because that permits an easier deployment.

## Todo

I most likely won't do it, but if you feel like it, it would be nice to 
- be able to configure the way sqlparse
- register the command in the package control

## License

This code is released under the MIT license.