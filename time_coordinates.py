def do_time(file):
    
    time = file.time
    start = round(float(time[0]*1000))   # start = 1961
    end = round(float(time[-1]*1000))    # end = 1990
    years = numpy.arange(start, end)
    months = numpy.arange(1, 13)
    
    dates = []
    for y in years:
        for m in months:
            dates.append(cftime.Datetime360Day(y, m, 16))
            
    new_data = file.assign_coords(time = dates)
    
    return new_data
