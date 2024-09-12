import json
import requests
import streamlit as st
import time
import google.generativeai as genai

GOOGLE_API_KEY = 'AIzaSyAIIN9YgLvn9Jkhb4roGRgTnugNgmqwDdY'
# All of places name , where we can vsit

destinations  = ['mysore palace', 'mysore zoo', 'sri chamundeshwari temple',
                "st. philomena's cathedral church", 'brindavan gardens',
                'karanji lake', 'jaganmohan palace art gallery and auditorium',
                'talakad', 'chamundi hills', 'lalitha mahal', 'ranganathittu bird sanctuary'
                ,'folk-lore museum mysore', 'railway museum',
                'devaraja market', 'shree shvetha varaha swamy temple',
                'regional museum of natural history mysore', 'melody world wax museum',
                'kukkarahalli lake', 'freedom fighter’s park', 'sanjeevini park', 'tipu sultan mosque',
                'lingambudhi lake', 'krs dam', 'grs fantasy park', 'avadhoota datta peetham',
                'lokaranjan aqua world underwater zoo','sri ranganathaswamy temple'
                 ]


# json file 
location_map = {'mysore palace': {
        	"cityNameKey": "mysore palace",
        	"placeURL": "http://www.mysorepalace.gov.in/",
        	"latitude": 12.305199,
        	"longitude": 76.654549,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 0
    	},
            'mysore zoo': {
        	"cityNameKey": "mysore zoo",
        	"placeURL": "https://mysuruzoo.info/",
        	"latitude": 12.301,
        	"longitude":76.6679,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 20,
        	"position": 1
    	},
			      "st. philomena's cathedral church" : {
        	"cityNameKey": "St. Philomena's Cathedral Church",
        	"placeURL": "https://mysorestphilomenachurch.com/",
        	"latitude": 12.321,
        	"longitude":76.6583,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 20,
        	"position": 2
    	},
    	"sri chamundeshwari temple" :
       {
        	"cityNameKey": "Shri Chamundeshwari Temple",
        	"placeURL": "https://chamundeshwaritemple.in/",
        	"latitude": 12.29192,
        	"longitude": 76.70446,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 20,
        	"position": 3
    	},
                "mysuru railway museum":
    	{
        	"cityNameKey": "MYSURU RAILWAY MUSEUM",
        	"placeURL": "",
        	"latitude": 12.3163,
        	"longitude": 76.6433,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 20,
        	"position": 4
    	},
                "jaganmohan palace art gallery and auditorium":
    	{
        	"cityNameKey": "Jaganmohan Palace Art Gallery And Auditorium",
        	"placeURL": "",
        	"latitude":12.30704280449335,
        	"longitude":  76.64988415327885,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 20,
        	"position": 5
    	},
                "lokaranjan aqua world underwater zoo":
    	{
        	"cityNameKey": "Lokaranjan Aqua World Underwater Zoo",
        	"placeURL": "https://underwaterzone.com/",
        	"latitude": 42.3449176,
        	"longitude": -71.0777013,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 20,
        	"position": 6
    	},
                "avadhoota datta peetham":
    	{
        	"cityNameKey": "Avadhoota Datta Peetham",
        	"placeURL": "https://www.dattapeetham.org/",
        	"latitude": 12.284619951803629,
        	"longitude": 76.65835248083995,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 20,
        	"position": 7
    	},
                "grs fantasy park":
    	{
        	"cityNameKey": " :GRS Fantasy Park",
        	"placeURL": "https://www.grsfantasypark.com/",
        	"latitude": 12.35325862195126,
        	"longitude": 76.63461487004324,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 20,
        	"position": 8
    	},
                "lalit mahal palace":
    	{
        	"cityNameKey": " Lalitha Mahal Palace",
        	"placeURL": "https://www.lalithamahalpalace.co.in/",
        	"latitude": 12.29825,
        	"longitude": 76.69233,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 9
    	},
                "regional museum of natural history mysore":
	{
        	"cityNameKey": "Regional Museum of Natural History Mysore",
        	"placeURL": "",
        	"latitude":12.3058620445,
        	"longitude":76.6744256244 ,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 10
    	},
                "brindavan gardens":
	{
        	"cityNameKey": "Brindavan Gardens",
        	"placeURL": "",
        	"latitude":12.426063,
        	"longitude":76.576276,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 11
    	},
                "folk-lore museum mysore":
	{
        	"cityNameKey": "Folk-Lore Museum Mysore",
        	"placeURL": "",
        	"latitude":12.313651,
        	"longitude":76.622322,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 12
    	},
                'devaraja market':
	{
        	"cityNameKey": "Devaraja Market",
        	"placeURL":"",
        	"latitude":12.310583,
        	"longitude":76.65209,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 13
    	},
                "shree shvetha varaha swamy temple":
	{
        	"cityNameKey": "Shree Shvetha Varaha Swamy Temple",
        	"placeURL": "",
        	"latitude":12.30334,
        	"longitude": 76.65511,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 14
    	},
                "karanji lake":
{
        	"cityNameKey": "Karanji Lake",
        	"placeURL": "",
        	"latitude": 12.303532292641751 ,
        	"longitude": 76.67343926774106,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 15
    	},
                "melody world wax museum":
{
        	"cityNameKey": "Melody World Wax Museum",
        	"placeURL": "",
        	"latitude": 12.302368565234856 ,
        	"longitude": 76.67756703793377,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 16
    	},
                "kukkarahalli lake":
{
        	"cityNameKey": "Kukkarahalli Lake",
        	"placeURL": "",
        	"latitude": 12.31372486181035 ,
        	"longitude": 76.63012677620505,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 17
    	},
                "freedom fighter's park":
{
        	"cityNameKey": " Freedom Fighter’s Park",
        	"placeURL": "",
        	"latitude": 12.302988977292605,
        	"longitude": 76.64607459560625,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 18
    	},
                "sanjeevini park":
{
        	"cityNameKey": "Sanjeevini Park",
        	"placeURL": "",
        	"latitude":  12.299707622087956 ,
        	"longitude": 76.62477817840748,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 19
    	},
                "lingambudhi park":
{
        	"cityNameKey": "Lingambudhi Lake",
        	"placeURL": "",
        	"latitude":  12.26987477881044,
        	"longitude": 76.61219250583693,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 20
    	},
                "krs dam":
{
        	"cityNameKey": "KRS Dam",
        	"placeURL": "",
        	"latitude":12.426320716258314,
        	"longitude": 76.57218132644493,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 21
    	},
                "talakad panchalinga temple":
{
        	"cityNameKey": "talakad panchalinga temple",
        	"placeURL": "",
        	"latitude": 12.182968772946744,
        	"longitude": 77.02742535403716,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 22
    	},
                "ranganathittu bird sanctuary":
{
        	"cityNameKey": "Ranganathittu Bird Sanctuary",
        	"placeURL": "",
        	"latitude": 12.424566739916589,
					"longitude": 76.65636659333653,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 23
    	},
                "sri ranganathaswamy temple":
{
        	"cityNameKey": "shri Ranganathaswamy Temple",
        	"placeURL": "",
        	"latitude": 12.4247524,
        	"longitude":  76.6797229,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 24
    	},
                "tipu sultan mosque":
{
        	"cityNameKey": "tipu sultan mosque",
        	"placeURL": "",
        	"latitude":12.4225459,
        	"longitude": 76.6891096,
        	"regionID": 1,
        	"open_time": "2024-02-13 00:00:00",
        	"close_time": "2024-02-13 23:30:00",
        	"service_time": 0,
        	"position": 25
    	},
           "chamundi hills":
        {
        	"cityNameKey": "chamundi hills",
        	"placeURL": "",
        	"latitude": 12.2757, 
        	"longitude": 76.6663,
        	"regionID": 1,
        	"open_time": "2022-03-11 10:00:00",
        	"close_time": "2022-03-11 10:00:00",
        	"service_time": 0,
        	"position": 26
    	},

                }


def postprocessing(text):
    location_json = []
    for i in text:
        if i.lower() in destinations:
            abc = location_map[i.lower()]
             
            location_json.append(abc)
    return location_json





# Function to preprocess stop sequences
def preprocess_stop_sequences(stop_sequences: str):
    if not stop_sequences:
        return None
    return [sequence.strip() for sequence in stop_sequences.split(",")]

# Function for the chatbot logic
def chatbot(text_prompt):
    text1 = f'''
        Tourist destinations in Mysore -
        Museums - Jaganmohan Palace Art Gallery and Auditorium, Folk-Lore Museum Mysore, Railway Museum, Regional Museum of Natural History Mysore, Melody World Wax Museum.
        Palace - Mysore palace, Lalit Mahal palace.
        Temples - Sri Chamundeshwari Temple, Sri Ranganathaswamy Temple, Shree Shvetha Varaha Swamy Temple, Avadhoota Datta Peetham, Talakad Panchalinga temple.
        Church - St. Philomena's Cathedral church.
        Gardens - Brindavan Gardens, Freedom Fighter’s Park, Sanjeevini Park, Kukkarahalli Lake, Lingambudhi Lake.
        Lakes - Karanji Lake.
        Hills - Chamundi Hills.
        Wildlife - Sri Chamarajendra Zoological Gardens,  Ranganathittu Bird Sanctuary, Lokaranjan Aqua World underwater Zoo.
        shopping - Devaraja Market.
        Dams - KRS Dam.
        Fun - GRS Fantasy Park.
        Mosque - Tipu sultan mosque.
        As a seasoned travel guide expert what 6 destinations would you recommend they visit?  
        Please mention only the destination names without providing additional details.'''
    text_prompt = text1
    
    genai.configure(api_key=GOOGLE_API_KEY)
    generation_config = genai.types.GenerationConfig(
        temperature=0.4,
        max_output_tokens=1024
    )
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(
        text_prompt,
        stream=True,
        generation_config=generation_config
    )

    # Streaming effect
    chatbot_response = ""
    for chunk in response:
        for i in range(0, len(chunk.text), 10):
            section = chunk.text[i:i + 10]
            chatbot_response += section
            time.sleep(0.01)
    return chatbot_response

# Streamlit app layout
st.set_page_config(
    page_title="MCG.AI: Mysuru Travel Guide",
    page_icon="🛫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Company logo and place logo
col1, col2 = st.columns([1, 9])
with col1:
    st.image("mcg_ai.jpeg", use_column_width="auto")

# Page style
st.markdown(
    """
    <style>
    body {
        background-color: purple;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Audio playback
#st.audio("sunshine.mp3", format="audio/mp3", start_time=0)

# Title and subtitle
st.title("MCG.AI: Mysuru Travel Guide")

# Text input for user prompt
text_prompt = st.text_input("Ask me places in Mysuru")

# Run button
roots = []
if st.button("Run"):
    # st.subheader("Follow the direction:")
    
    # Generate and display chatbot response
    chatbot_response = chatbot(text_prompt)
    st.write("Input:", text_prompt)
    st.write("Output:")
    places  = [place.strip() for place in chatbot_response.split("\n") if place.strip()]
    for place in places:
        st.write(place)
        place = str(place.split(". ",1)[1])
        roots.append(place)
        
    json_file = postprocessing(roots)
    data_destination = {
        "first_name": "MCG",
        "last_name": "AI",
        "organization": "Mysuru",
        "travel_time": 5,
        "locations": json_file
    }
    json_format = json.dumps(data_destination, indent=4)
    
    #st.write(json_format)
    
    url = 'http://voyagen.us-east-2.elasticbeanstalk.com/application/post/'

    response = requests.post(url, json=data_destination)



    key = response.json()['Query Identifier']

    url2 = 'http://voyagen.us-east-2.elasticbeanstalk.com/application/get/'
    response2 = requests.get(url2 + key)
    text_content = response2.text


    data = json.loads(text_content)
    st.subheader("Follow the direction:")
    st.write(data['shortest_path'])
    st.write('shortest-distance->')
    st.write(data["shortest_distance"])

# Sidebar note about Google API Key
st.sidebar.markdown("Note: Provide your own GOOGLE_API_KEY for this app to function properly.")













