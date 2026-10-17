"""Dashboard de pilotage fictif; lit les données versionnées du dépôt."""
import json
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
ROOT=Path(__file__).resolve().parents[1]
ref=json.loads((ROOT/'data/referentiel.json').read_text(encoding='utf8'))
pilot=json.loads((ROOT/'data/pilotage.json').read_text(encoding='utf8'))
backlog=pd.read_csv(ROOT/'docs/pilotage/backlog.csv')
stories=backlog[backlog['type']=='Story']
risk=pd.read_csv(ROOT/'docs/pilotage/registre-risques.csv')
st.set_page_config(page_title='DéclaSinistre — pilotage',page_icon='💧',layout='wide')
st.title('DéclaSinistre | tableau de pilotage')
st.caption('Cas pratique fictif · backlog et sprints simulés · objectifs métier non mesurés')
done=int(stories['statut'].str.startswith('Terminé').sum()); total=len(stories)
a,b,c=st.columns(3);a.metric('Stories terminées',f'{done}/{total}',help='Source backlog.csv; stories marquées terminées dans une simulation.');b.metric('Avancement simulé',f'{done/total:.0%}',help='Terminées ÷ stories totales; pas un résultat de projet réel.');c.metric('Tests produit exécutés','Non disponible',help='Pas de résultats navigateur enregistrés.')
st.subheader('Backlog et priorité MoSCoW')
st.plotly_chart(px.histogram(stories,x='priorite',color='statut',barmode='group'),use_container_width=True)
st.subheader('Vélocité simulée')
sprints=pd.DataFrame([{'Sprint':s['name'],'SP terminés':s['done'],'Capacité hypothétique':s['start_capacity']} for s in pilot['sprints']])
st.plotly_chart(px.bar(sprints,x='Sprint',y='SP terminés',text='SP terminés'),use_container_width=True)
st.caption('Story points relatifs, inventés pour le scénario. La vélocité ne mesure ni la performance individuelle ni une productivité universelle.')
st.subheader('Burndown simulé')
rows=[]
for s in pilot['sprints']:
 for day,left in enumerate(s['remaining_daily']):rows.append({'Sprint':s['name'],'Jour':day,'SP restants':left})
st.plotly_chart(px.line(pd.DataFrame(rows),x='Jour',y='SP restants',color='Sprint',markers=True),use_container_width=True)
st.caption('Source unique: data/pilotage.json; SP restants illustratifs par jour, y compris un reliquat simulé.')
st.subheader('Risques')
risk['Criticité P×I']=risk['probabilite_1_5']*risk['impact_1_5']
st.dataframe(risk,use_container_width=True,hide_index=True)
st.subheader('Couverture des exigences')
testable=[r for r in ref['requirements'] if r['testable']]
covered=sum(any(r['id'] in t['links'] for t in ref['tests']) for r in testable)
st.metric('Exigences testables liées à un cas',f'{covered}/{len(testable)}',help='Calcul depuis referentiel.json; lien de traçabilité prévu, pas preuve d’exécution.')
st.subheader('Indicateurs métier : hypothèses et cibles')
st.dataframe(pd.DataFrame([
 {'Indicateur':'Taux de dossiers incomplets','Hypothèse initiale':'30 %','Cible':'≤10 %','Formule':'Dossiers nécessitant relance ÷ dossiers reçus','Statut':'Non mesuré'},
 {'Indicateur':'Prise en charge initiale','Hypothèse initiale':'5 jours','Cible':'≤1 jour ouvré','Formule':'Dépôt à première prise en charge humaine','Statut':'Non mesuré'},
 {'Indicateur':'Durée déclaration','Hypothèse initiale':'À mesurer','Cible':'<5 minutes','Formule':'Médiane début→confirmation nominale','Statut':'Non mesuré'}]),use_container_width=True,hide_index=True)
st.info('Aucune connexion assureur, aucun dépôt distant et aucun résultat réel. Les valeurs d’état et de sprint sont des simulations.')
