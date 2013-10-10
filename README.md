# format_sql

Added possibility to format SQL queries in sublime text 3 through the 'format_sql' command. It takes some poorly formatted SQL code like this :

	select * from STuff s where s.something > 42 limit 30

and turns it into this :

	SELECT *
	FROM stuff s
	WHERE s.something > 42 LIMIT 30

Yep, I know. That's pretty awesome. Well, I'm not so sure about that, but anyway, that's really useful to me.

## Installation

Clone this repository inside of the Packages/User repository, then map the new command to a key binding

## Usage

Create the following binding in Preference / Key Bindings - User
	
	{ "keys": ["ctrl+alt+f"], "command": "format_sql" }
