# Data Analysis Scripts

## Setup

    Edit generateData.sh:7 to grab the data you want.
      Date format is yyyy-mm-dd-hh
      Where any field can be replaced with a range e.g. dd = {01..07}, to grab the first seven days of a month.
      Annoyingly enough, months and days start at 01 and hours start at 0

    Run generateData.sh with './generateData.sh'
      The script may need to have its access permissions changed to allow it to be exectuted with 'chmod +x generateData.sh'

## Scripts and what they do

    languages.py
      Iterates over entries in a data file finding PushEvents and grabs the language distribution of the associated repo
          HTTP errors are output to errorLog

    EventDistro.py
      Iterates over entries in a data file to find the amount of each kind of event present

    RepeatedRepo.py
      Iterates over data files and analyzes the amount of API requests required for the workload by the level of optimization

## Running the scripts

    Run RepeatedRepo.py with 'python3 RepeatedRepo.py'
      Output goes to commandline, can be redirected to a file

    languages.py does not currently work with OAuth tokens, limited to 60 requests/hr
      urllib request needs additional OAuth headers
      urllib.request.Request(url, data=None, headers={username:OAuth_Token}, origin_req_host=None, unverifiable=False, method=None)
