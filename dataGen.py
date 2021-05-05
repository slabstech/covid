# import required module
import os,calendar;

import yaml

# assign directory
directory = '_data'

# itrate over files in
# that directory


for filename in os.listdir(directory):
    if 'covid' in filename:
        #covid-day-status-2020.yaml extract year
        year=filename[17:21]
        print(year)

        stats_path="_posts/stats/" + year
        print(stats_path)
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
                #print(data)

                for result in data:
                    #print(result)

                    f = open("demofile2.txt", "w")



                    f.write(result['day'])
                    f.write(result['active'])
                    f.write(result['total'])
                    f.write(result['recovered'])
                    f.write(result['deceased'])
                    f.write(result['new_case'])
                    if 'icu' in result:
                        f.write(result['icu'])
                    if 'vaccinated' in result:
                        f.write(result['vaccinated'])

                    f.close()

                    print(result['day'])
                    print(result['active'])
                    print(result['total'])
                    print(result['recovered'])
                    print(result['deceased'])
                    print(result['new_case'])
                    if 'icu' in result:
                        print(result['icu'])
                    if 'vaccinated' in result:
                        print(result['vaccinated'])

            except yaml.YAMLError as exc:
                print(exc)


#    f = os.path.join(directory, filename)
    # checking if it is a file
#    if os.path.isfile(f):
#        print(f)
