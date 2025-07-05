from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="USER_API_KEY",  # Replace with your actual OpenRouter API key
)

def instructor_chatbot():
    """Command-line AI Itinerary Chatbot."""
    print("Welcome to AI Itinerary recommender! Answer a few questions to get personalized itinerary advice.\n")
    
    days = input("How many (days): ")
    location = input("Where is the destination (city name): ")
    age = input("Enter your age: ")
    
    prompt = f"""
    Generate a detailed {days}-day itinerary for {location}, New Zealand, for a {age}-year-old traveler.
    The itinerary should include visits to landmarks, museums, and popular local restaurants.
    Ensure there is a balance between guided tours and free time for exploration.
    Each day should have suggestions for breakfast, lunch, and dinner, with brief descriptions of each activity and restaurant.
    The traveller has never been to South island before and wants to experience both the well-known and hidden gems of the city.
    They are particularly interested in activities. They do not prefer to use public transport and enjoy walking tours.
    Give a structured itinerary with a name of the place, address, and short description for each day separately in order with a maximum of three activities in a day.
    """

    try:
        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat:free",  # Correct model name for OpenRouter
            messages=[
                {"role": "system", "content": "You are a professional itinerary recommender."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        print("\nMy Name is Hadi as AI Itinerary expert:")
        print(completion.choices[0].message.content)
    except Exception as e:
        print("Error communicating with OpenRouter API:", e)

if __name__ == "__main__":
    instructor_chatbot()