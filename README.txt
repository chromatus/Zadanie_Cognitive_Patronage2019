This is application made for Intive Patronage 2019.

It creates very simple django WWW page, working on sqlite3 database. 
It contains 3 views:
- main menu - contains only clickable links to other views
	loaded from template
- data table presentation - puts all the data from the database
	into single html table. Only this table and clickable link
	to the main menu are present on this view.
	loaded from template
- data filtration form - simple form with 4 fields to fill:
	- minimum salary
	- maximum salary
	- minimum years worked
	- maximum years worked
	Under those fields there are return and continue buttons.
	After continue button is pressed, the form is sent to 'filtered' view
- filtered - presents data from the database, that fit the criteria from
	the form, in html table. Under the table there's clickable link
	to the main menu.
- data import - loads data from file, and puts it into the database.
	Incomplete rows are filled by prediction algorithms, values are 
	predicted based on data from complete rows. When that is complete
	confirmation message is displayed.

django superuser:
	login: admin
	password: admin
	

Planned features:
- data presentation with charts