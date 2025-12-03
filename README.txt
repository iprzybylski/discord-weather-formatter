DiscordWeatherFormatter

About:

    DiscordWeatherFormatter is a Python tool for quickly formatting manually-inputted
    weather data to be posted into a discord server. 

Usage:

    For general use, simply run the runner.py script. You will be asked whether you would
    like to format hourly or multiday data. Type 'm' for multiday formatting. Type 'h' for
    hourly data. 

    Multiday Formatting:

        You will be prompted to enter data for 5 days starting tomorrow. 

        Following the prompt <Day>: enter your data in the following format:

            <low temp> <high temp> <weather code>

            for a list of weather codes, see the 'weather codes' section below. 

        For more control over the timeframe of the forecast, you can call the format_multiday(int, int)
        function directly by importing it from formatter.py. You can adjust the num_days variable
        and the today_variable, which is set by default to today, where sunday = 0, monday = 1, etc. 

    Hourly Formatting:

        You will be prompted to enter data for 7am, 10am, 1pm, 4pm, 7pm. Enter your data
        int the following format:

            <temp> <weather code>

            for a list of weather codes, see the 'weather codes' section below. 

        For more control over the timeframe of the forecast, you can call the format_hourly(int, int, int)
        function directly by importing it from formatter.py. You can adjust the start and end times and the 
        increment (min 1 hour, default 3 hours). 

    Copy the output of the program from the terminal and paste it into discord. 

    Weather Codes:

        The table below details the weather codes for supported weather conditions

        s : clear
        ms: mostly clear
        pc: partly clear
        mc: mostly cloudy
        c : cloudy
        f : foggy
        w : windy
        ra: rain
        sn: snow
        lr: showers
        ss: snow showers
        mx: wintry mix
        fr: freezing rain
        it: isolated thunderstorms
        st: scattered thunderstorms
        t : thunderstorms

    in formatter.py:

        format_multiday(num_days) prompts the user to enter weather conditions for 
        num_days days in the format <low temp> <high temp> <weather code>. 