from django.shortcuts import render
import datetime
from jalali_date import date2jalali,datetime2jalali
from datetime import timedelta
# Create your views here.
t = [datetime.datetime.now()]
t[0] = datetime.datetime.now()
year = [int(str('14' + str(datetime2jalali(datetime.datetime.now()).strftime('%y'))))]
year[0] =int(str('14' + str(datetime2jalali(datetime.datetime.now()).strftime('%y'))))
calandar_array_for_show = ['0']
calandar_array_for_show[0] ='0'
calandar_array_for_miladidate = [datetime.datetime.now()]
calandar_array_for_miladidate[0] = datetime.datetime.now()
calandar_array_for_shamsidate = [str(datetime2jalali(t[0]).strftime('%y %b %d %a'))]
calandar_array_for_shamsidate [0] = str(datetime2jalali(t[0]).strftime('%y %b %d %a'))
def strb(tdef):
    x = str(datetime2jalali(tdef).strftime('%a %d %b %y'))
    rmonth = x[7:10]
    ag_month = rmonth
    if ag_month == 'Far':
        ag_month = 'فروردین'
    if ag_month == 'Ord':
        ag_month = 'اردیبهشت'
    if ag_month == 'Kho':
        ag_month = 'خرداد'
    if ag_month == 'Tir':
        ag_month = 'تیر'
    if ag_month == 'Mor':
        ag_month = 'مرداد'
    if ag_month == 'Sha':
        ag_month = 'شهریور'
    if ag_month == 'Meh':
        ag_month = 'مهر'
    if ag_month == 'Aba':
        ag_month = 'آبان'
    if ag_month == 'Aza':
        ag_month = 'آذر'
    if ag_month == 'Dey':
        ag_month = 'دی'
    if ag_month == 'Bah':
        ag_month = 'بهمن'
    if ag_month == 'Esf':
        ag_month = 'اسفند'
    rmonth = ag_month
    return (rmonth)
def strd(tdef):
    x = str(datetime2jalali(tdef).strftime('%a %d %b %y'))
    rday = x[4:6]
    if rday == '01':
        rday = '1'
    if rday == '02':
        rday = '2'
    if rday == '03':
        rday = '3'
    if rday == '04':
        rday = '4'
    if rday == '05':
        rday = '5'
    if rday == '06':
        rday = '6'
    if rday == '07':
        rday = '7'
    if rday == '08':
        rday = '8'
    if rday == '09':
        rday = '9'
    return (rday)
def stra(tdef):
    x = str(datetime2jalali(tdef).strftime('%a %d %b %y'))
    rweek = x[0:3]
    if rweek == 'Sat':
        rweek = 'شنبه'
    if rweek == 'Sun':
        rweek = 'یکشنبه'
    if rweek == 'Mon':
        rweek = 'دوشنبه'
    if rweek == 'Tue':
        rweek = 'سه‌شنبه'
    if rweek == 'Wed':
        rweek = 'چهارشنبه'
    if rweek == 'Thu':
        rweek = 'پنج‌شنبه'
    if rweek == 'Fri':
        rweek = 'جمعه'
    return (rweek)
def stry(tdef):
    x = str(datetime2jalali(tdef).strftime('%a %d %b %y'))
    ryear = x[11:]
    return (ryear)
def stradb(tdef):
    r = stra(tdef)+' '+strd(tdef)+' '+strb(tdef)
    return (r)
def stradby(tdef):
    r = stra(tdef)+' '+strd(tdef)+' '+strb(tdef)+' '+stry(tdef)
    return (r)
def stryabd(tdef):
    r = stry(tdef)+' '+stra(tdef)+' '+strb(tdef)+' '+strd(tdef)
    return (r)
def stryadb(tdef):
    r = stry(tdef)+' '+stra(tdef)+' '+strd(tdef)+' '+strb(tdef)
    return (r)
def strn():
    tx = datetime.datetime.now()
    r = stry(tx)+' '+stra(tx)+' '+strd(tx)+' '+strb(tx)
    return (r)
def strbd(tdef):
    r = strb(tdef)+' '+strd(tdef)
    return (r)

def addcantact(request):
    bbtn = request.POST.get("bbtn")
    button_year = request.POST.get("button_year")
    if (button_year == None) or (button_year == ''):
        button_year = str(year[0])
    button_upmounth = request.POST.get("button_upmounth")
    button_downmounth = request.POST.get("button_downmounth")
    button_calandar = request.POST.get("addcantact")

    if (bbtn != None) and (bbtn != '') and (calandar_array_for_show != None) and (calandar_array_for_show != '') :
        return render(request, 'add_cantact.html', context={'berthday_shamsi':calandar_array_for_shamsidate[int(bbtn)],
                                                            "berthday_miladi":datetime.datetime.date(calandar_array_for_miladidate[0]).strftime('%a %d %b %y') ,
                                                            })
    if(button_year != None) and (button_year != ''):
        if int(button_year) < 1200:
            button_year = 1402
        if int(button_year) > int(str('14' + stry(datetime.datetime.now()))):
            button_year = str(year[0])
        mounth_of_t = strb(t[0])
        while int(button_year) != year[0] :
            if int(button_year) < year[0] :
                if (strb(t[0]) == 'فروردین') and (strd(t[0]) == '1'):
                    year[0] -= 1
                    button_calandar = "accept"
                    button_upmounth = None
                    button_downmounth = None
                t[0] -= timedelta(days=1)
            if int(button_year) > year[0] :
                if (strb(t[0]) == 'فروردین') and (strd(t[0]) == '1'):
                    year[0] += 1
                    button_calandar = "accept"
                    button_upmounth = None
                    button_downmounth = None
                t[0] += timedelta(days=1)

        if strb(t[0]) == 'اسفند' :
            while strb(t[0]) != mounth_of_t :
                t[0] -= timedelta(days=1)
        if strb(t[0]) == 'فروردین' :
            while strb(t[0]) != mounth_of_t :
                t[0] += timedelta(days=1)

    if button_upmounth == "accept" :
        button_calandar = "accept"
        mounth = strb(t[0])
        while strb(t[0]) == mounth :
            t[0] += timedelta(days=1)
        if strb(t[0]) == 'فروردین' :
            year[0] += 1

    if button_downmounth == "accept" :
        button_calandar = "accept"
        mounth = strb(t[0])
        while strb(t[0]) == mounth :
            t[0] -= timedelta(days=1)
        if strb(t[0]) == 'اسفند' :
            year[0] -= 1
    if button_calandar == "accept" :
        mounth = strb(t[0])
        day_of_mounth = strd(t[0])
        day_of_week = stra(t[0])
        r = 0
        g = 0
        calandar_array_for_show.clear()
        calandar_array_for_miladidate.clear()
        calandar_array_for_shamsidate.clear()

        for r in range(int(day_of_mounth)) :
            t[0] -= timedelta(days=1)

        while stra(t[0]) != 'جمعه' :
            print(stra(t[0]))
            t[0] -= timedelta(days=1)
            calandar_array_for_show.append('')
            calandar_array_for_miladidate.append(t[0])
            calandar_array_for_shamsidate.append(stradby(t[0]))

        calandar_array_for_show.append('')
        calandar_array_for_miladidate.append(t[0])
        calandar_array_for_shamsidate.append(stradby(t[0]))
        while strd(t[0]) != "1" :
            t[0] +=timedelta(days=1)
        i = 0
        while strb(t[0]) == mounth :
            i += 1
            calandar_array_for_show.append(i)
            calandar_array_for_miladidate.append(t[0])
            calandar_array_for_shamsidate.append(stradby(t[0]))
            t[0] += timedelta(days=1)
        t[0] -=timedelta(days=1)

        return render(request,'calander.html',context={"year" : year[0],
                                                        "mounth": mounth,
                                                        "calandar_aray":calandar_array_for_show,
                                                       })
    return render(request,'add_cantact.html')