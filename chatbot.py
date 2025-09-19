import random
import re

class SimpleBot:
    """Simple rule-based chatbot - easily replaceable with LLM API"""
    
    def __init__(self):
        self.responses = {
            'greeting': [
                "Hello! I'm delighted to help you today. What can I assist you with?",
                "Hi there! It's my pleasure to help you. How may I be of service?",
                "Hey! I'm here and happy to assist you with anything you need."
            ],
            'goodbye': [
                "Thank you for chatting with me! Have a wonderful day!",
                "It was great talking with you! Take care and stay safe!",
                "Goodbye! I hope I was helpful. Have a fantastic day!"
            ],
            'help': [
                "I'm GUIDEBOT, and I'm here to kindly assist you with any questions, especially about traffic safety!",
                "I'd be happy to help with various topics. Please let me know what you'd like to learn about.",
                "I'm here to guide you with care. What would you like to know? I'm particularly knowledgeable about traffic rules!"
            ],
            'default': [
                "That's quite interesting! I'd love to hear more about that.",
                "I appreciate you sharing that. Is there anything else I can help you with today?",
                "Thank you for telling me that! How else may I assist you?",
                "I see, that's good to know. Please feel free to ask me anything else!"
            ]
        }
        
        # Traffic knowledge base with polite responses
        self.traffic_kb = {
            'red light': "Great question! When you see a red light, please come to a complete stop and wait patiently until it turns green.",
            'yellow signal': "I'm happy to explain! A yellow signal means you should prepare to stop safely, as the light will turn red soon.",
            'green light': "Excellent question! When the light is green, you may proceed, but please check carefully for pedestrians and other vehicles first.",
            'speed limit': "I'd be glad to help! Please follow posted speed limits for everyone's safety. Typically: 25-35 mph in cities, 55-80 mph on highways.",
            'zebra crossing': "Thank you for asking! A zebra crossing is a pedestrian crossing area where you should always kindly yield to pedestrians.",
            'road safety rules': "I'm pleased to share these important safety rules: 1. Always wear your seatbelt 2. Never drink and drive 3. Follow speed limits 4. Use turn signals 5. Keep a safe distance 6. Avoid using your phone while driving",
            'stop sign': "Great safety question! At a stop sign, please come to a complete stop, look both ways carefully, then proceed when it's safe.",
            'traffic rules': "I'm happy to help! Please follow all traffic signals, maintain speed limits, use your indicators, and always stay alert for everyone's safety.",
            'parking rules': "Thank you for being considerate! Please park only in designated areas and avoid blocking driveways or fire hydrants.",
            'right of way': "Excellent question! Please kindly yield to pedestrians, emergency vehicles, and follow traffic signal priority.",
            'roundabout': "I'm glad you asked! Please enter when clear, yield courteously to traffic already in the roundabout, and signal your exit.",
            'school zone': "Thank you for caring about children's safety! Please reduce speed to 15-25 mph during school hours and watch carefully for children crossing.",
            'emergency vehicle': "Important safety question! Please pull over to the right and stop when you hear sirens or see flashing lights.",
            'drunk driving': "I appreciate your responsibility! Please never drive under the influence. Kindly use a taxi, rideshare, or designated driver instead.",
            'seatbelt': "Wonderful safety question! Please always wear your seatbelt - it reduces risk of death by 45% and serious injury by 50%.",
            'turn signal': "Great question! Please use your indicators 100 feet before turning in the city, and 300 feet on the highway.",
            'following distance': "Excellent safety question! Please maintain the 3-second rule: stay at least 3 seconds behind the vehicle ahead.",
            'blind spot': "Thank you for asking about safety! Please check your mirrors and look over your shoulder before changing lanes.",
            'pedestrian': "I'm glad you're being considerate! Please always yield kindly to pedestrians at crosswalks and intersections.",
            'bicycle': "Great question about sharing the road! Please give cyclists 3 feet of space when passing and check for bike lanes.",
            'construction zone': "Thank you for asking! Please slow down, merge early, and follow flaggers and posted signs for everyone's safety.",
            'weather driving': "Excellent safety question! Please reduce speed in rain/snow, increase following distance, and use your headlights.",
            'highway merging': "I'm happy to help! Please match traffic speed, use the acceleration lane, and signal when it's safe to merge.",
            'u-turn': "Good question! Please only make U-turns where legal and safe, and kindly yield to all traffic and pedestrians.",
            'horn': "Thank you for asking! Please use your horn to warn others of danger, not to express anger or frustration.",
            'headlights': "Great safety question! Please use headlights 30 minutes before sunset to 30 minutes after sunrise.",
            'cell phone': "I appreciate your safety concern! Please use hands-free only while driving, or pull over safely to make calls or text.",
            'road rage': "Important question! Please stay calm, don't engage with aggressive drivers, and report dangerous behavior if needed.",
            'tire pressure': "Excellent maintenance question! Please check monthly - proper pressure improves safety and fuel efficiency.",
            'brake': "Great safety question! Please test your brakes regularly and maintain a safe following distance for stopping."
        }
    
    def get_response(self, message):
        """Generate bot response based on user message"""
        message = message.lower().strip()
        
        # Check for traffic-related keywords first
        traffic_keywords = ['traffic', 'signal', 'light', 'road', 'speed', 'zebra', 'crossing', 'stop', 'parking', 'right of way', 'roundabout', 'school', 'emergency', 'drunk', 'seatbelt', 'turn', 'following', 'blind', 'pedestrian', 'bicycle', 'construction', 'weather', 'highway', 'u-turn', 'horn', 'headlight', 'cell phone', 'road rage', 'tire', 'brake', 'red', 'yellow', 'green']
        if any(keyword in message for keyword in traffic_keywords):
            traffic_response = self.get_traffic_response(message)
            if traffic_response:
                return traffic_response
        
        # Greeting patterns
        if re.search(r'\b(hi|hello|hey|greetings)\b', message):
            return random.choice(self.responses['greeting'])
        
        # Goodbye patterns
        elif re.search(r'\b(bye|goodbye|see you|farewell)\b', message):
            return random.choice(self.responses['goodbye'])
        
        # Help patterns
        elif re.search(r'\b(help|assist|support|guide)\b', message):
            return random.choice(self.responses['help'])
        
        # Default response
        else:
            return random.choice(self.responses['default'])
    
    def get_traffic_response(self, message):
        """Find matching traffic response from knowledge base"""
        # Check for traffic light combinations first
        if any(word in message for word in ['red', 'yellow', 'green']) and 'light' in message:
            return "I'm happy to explain traffic lights! 🚦 RED LIGHT: Stop and wait until it turns green. YELLOW LIGHT: Prepare to stop safely, as it will turn red soon. GREEN LIGHT: You may proceed, but please check for pedestrians and vehicles first. Always follow traffic signals for everyone's safety!"
        
        # Check individual traffic topics
        for key, answer in self.traffic_kb.items():
            if key in message:
                return answer
        
        # Polite fallback for traffic-related questions without exact matches
        return "Thank you for your traffic-related question! While I don't have specific information about that, I encourage you to check with your local traffic authority or driving manual for accurate guidance. Is there anything else about traffic safety I can help you with?"

# Initialize bot instance
bot = SimpleBot()