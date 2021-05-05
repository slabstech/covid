# import required module
import os,calendar;
from time import strptime
import yaml

# assign directory
directory = '_data'

# itrate over files in
# that directory


for filename in os.listdir(directory):
    if 'covid' in filename:
        #covid-day-status-2020.yaml extract year
        year=filename[17:21]
        #print(year)

        stats_path="_posts/stats/" + year

        #print(stats_path)
        if not os.path.isdir(stats_path):
            print("")
            try:
                os.mkdir(stats_path)
                #[os.mkdir(stats_path+"/"+m) for m in calendar.month_name if m]
            except OSError:
                print ("Creation of the directory %s failed" % stats_path)
            else:
                print ("Successfully created the directory %s " % stats_path)

        for m in calendar.month_name :
            month_path=stats_path+"/"+m
            if not os.path.isdir(month_path):

                try:
                    os.mkdir(month_path)
                except OSError:
                    print ("Creation of the directory %s failed" % month_path)
                else:
                    print ("Successfully created the directory %s " % month_path)


        with open(os.path.join(directory,filename), 'r') as stream:
            try:
                #print(yaml.safe_load(stream))
                data = yaml.safe_load(stream)

                for result in data:
                    #print(result)

                    #2020-07-24-case-update-july-24

                    date = result['day'].split("-")

                    month_int = strptime(date[1],'%b').tm_mon
                    month_str=str(month_int)

                    date_str = month_str+  '-' + date[0]
                    case_file=year+ '-' + date_str +'-case-update-'+ date[1] + '-' + date[0] +'.md'

                    case_file_path = stats_path + "/" + calendar.month_name[month_int] + "/" + case_file

                    #print(case_file_path )
                    #print(case_file)

                    if not os.path.isfile(case_file_path):

                        f = open(case_file_path, "w")

                        f.write('---  \n'\
                        'layout: post \n'\
                        'title:  "Covid Updates for ' + date[0] + '-'+ calendar.month_name[month_int]+ '-'+ year + '" \n'\
                        'date:   '+ year+ '-' + date_str  + ' 13:20:40 +0530 \n'\
                        'categories: stats \n'\
                        '--- \n\n'\

                        'Hubballi - Dharwad District \n\n'\

                        'No. of Cases > '+result['total']+ ' \n\n'\

                        'No. of Active > '+result['active']+ ' \n\n'\

                        'No. of New Case > '+result['new_case']+ ' \n\n'\

                        'No. of Recovered > '+ result['recovered'] + ' \n\n'\

                        'No. of Deceased > '+ result['deceased'] + ' \n\n'\


                        )


                        if 'icu' in result:
                            f.write('No. of ICU Cases > '+ result['icu'] + '\n\n')
                        if 'vaccinated' in result:
                            f.write('No. of Vaccination Done > '+ result['vaccinated']+ '\n\n')

                        f.write('View All Stats at [https://slabs.tech/covid/stats/](https://slabs.tech/covid/stats/)')
                        f.close()

            except yaml.YAMLError as exc:
                print(exc)


#    f = os.path.join(directory, filename)
    # checking if it is a file
#    if os.path.isfile(f):
#        print(f)
