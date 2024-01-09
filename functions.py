from datetime import datetime , timedelta
import globals

def get_weekdates(date: str, previous_week: bool = False, next_week: bool = False) -> list[str]:
    """Par default renvoi la semaine actuelle"""
    
    dates = []
    
    formatage_date = datetime.strptime(date, "%d/%m/%Y")     
    nom_jour = formatage_date.strftime("%A")               
    nb_jour = globals.JOURS_NUMEROTES[nom_jour]
    
    if previous_week:
        week = formatage_date - timedelta(days=nb_jour+7)
    elif next_week:
        week = formatage_date + timedelta(days=7-nb_jour)
    else:
        week = formatage_date - timedelta(days=nb_jour)

    dates = [(week + timedelta(days=i+1)).strftime("%d/%m/%Y") for i in range(7)]
        
    return dates

def get_plage_dates(dates: list[str]) -> str:
    
    start_date = datetime.strptime(dates[0], "%d/%m/%Y").strftime("%d %B")
    end_date = datetime.strptime(dates[-1], "%d/%m/%Y").strftime("%d %B %Y")
    
    return f"{start_date} - {end_date}"