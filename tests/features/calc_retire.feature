Feature:
	Calculating retirement age

	Scenario: Exiting the program
		Given The prompt “Enter the year of birth or <enter> to exit””
		When The user presses the “Enter” key
		Then The program will end

	Scenario Outline: Entering a valid birth year
		Given The prompt “Enter the year of birth or <enter> to exit””
		When The user enters a valid birth year EX: 1998
		Then The program will store and use it to calculate retirement age later
		Examples:









	Scenario: Entering invalid birth year:
		Given The prompt “Enter the year of birth or <enter> to exit””
		When The user enters an invalid birth year EX: 2050
		Then The program will tell user it is an invalid year before stopping.

	Scenario: Entering a valid birth month:
		Given The prompt “Enter the month of birth”
		When The user enters a valid birth month, anything between 1-12
		Then The program will store birth month to calculate and show retirement age and date.

	Scenario: Entering invalid birth month:
		Given The prompt “Enter the month of birth”
		When The user enters an invalid birth month. Anything that isn’t a number 1-12.
		Then The program will tell user it is an invalid month before stopping.




Scenario: Entering all valid inputs
	Given: The prompts for birth month and year
When: The user enters valid birth year and month
	Then: The program will print “your full retirement age is <retirement year age> and <retirement month age> months
this will be in <retirement year date> of <retirement month date>” according to the retirement table.
