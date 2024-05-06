import text_gen as gen
import random

env = {}
env["current_chapter"] = 1
env["story_length"] = 3
env["theme"] = "A space adventure on the moon, where a child is playing with an alien."
env["person_type"] = "First"
env["creature"] = "human"
env["name"] = "Jeff"
env["history"] = "" 

art = {}
art["Art style"] = "Realistic"
art["gender"] = "Male"
art["age"] = "10"
art["eye color"] = "green"
art["hair color"] = "brown"
art["height"] = "4 feet 11 inches"
art["top color"] = "white"
art["top"] = "shirt"
art["bottom color"] = "black"
art["bottom"] = "long pants"
art["emotion"] = "scared"
art["shoes"] = "sneakers"
art["chapter"] = "They are an average 10 year old, but their life is about to change. Coming from the sky was a meteorite, heading right towards them. They begin to run away. They are in the middle of the woods."

art["bd"] = ["strong", "old", "young", "weak", "beutiful", "bold"]
art["body description"] = art["bd"][random.randint(0, len(art["bd"]) - 1)]
art["second body description"] = art["bd"][random.randint(0, len(art["bd"]) - 1)]
art["third body description"] = art["bd"][random.randint(0, len(art["bd"]) - 1)]
art["dcs"] = ["a long dress, high heels, and makeup", "long shorts, loose jersey, and a basketball cap"]
art["dc"] = art["dcs"][random.randint(0, len(art["dcs"]) - 1)]
print(art["Art style"], art["gender"], art["body description"], art["second body description"], art["third body description"], art["dc"])
#respo = gen.intro_prompt(env)
art['gender'] = "male"
respo = f"""
Generate images using this exact template:

{art["Art style"]} painting of a {art["gender"]} who is {art["body description"]}, {art["second body description"]}, and {art["third body description"]}. It should incorporate gradient shading, clean linework, 
vibrant palette, and stylized proportions. Wearing {art["dc"]}. The subject of the art should be in this scenario:

They are an average 10 year old, but their life is about to change. Coming from the sky was a meteorite, heading right towards them. They begin to run away.

 """

respo2 = f"""
Generate images using this exact template:

A realistic painting of a {art["gender"]} about {art["age"]}. They should have {art["eye color"]} eyes, {art["hair color"]} hair, about {art["height"]} tall, and is {art["emotion"]}. It should incorporate gradient shading, clean linework, 
vibrant palette, and stylized proportions. They should be wearing a {art["top color"]} {art["top"]}, {art["bottom color"]} {art["bottom"]} that are slightly too big, and {art["shoes"]}. The subject of the art should be in this scenario:

{art["chapter"]}

 """
text1 = "Once upon a time, in a quaint village nestled between rolling hills and lush forests, there lived a curious fox named Felix. Every night, under the shimmering moonlight, Felix would embark on daring adventures through the enchanted woods, guided by his keen senses and adventurous spirit. His friends, the wise old owl and the playful rabbit, often joined him on these escapades, weaving tales of magic and wonder as they roamed the starlit paths. Together, they discovered hidden treasures, encountered mysterious creatures, and forged bonds that would last a lifetime, creating their own timeless tale of friendship and courage."
text2 = "One fateful night, as they ventured deeper into the heart of the forest, they stumbled upon a forgotten ruin veiled in shadows. Intrigued by the secrets it held, they braved its crumbling halls, unaware of the ancient magic that lay dormant within. With each step, whispers of the past echoed through the corridors, beckoning them towards an ancient artifact that promised untold power. But as they reached out to claim it, the magic stirred, revealing a guardian whose eyes blazed with ancient fury. In a moment of clarity, Felix realized that true strength lay not in the pursuit of power, but in the bonds of friendship and the courage to face the unknown together. With a shared glance, they turned away from the allure of the artifact, their hearts filled with the knowledge that their greatest adventures were yet to come."
text1 = "In the bustling city of Ember Grove, amidst the towering skyscrapers and bustling streets, lived a young artist named Lily. With a paintbrush in hand and dreams in her heart, she navigated the urban jungle, seeking inspiration in every corner. One day, while lost in thought by the riverbank, she stumbled upon an old, forgotten mural, its colors faded but its story vivid. Intrigued, Lily embarked on a quest to restore the mural to its former glory, uniting the community in a shared vision of hope and resilience. Through her art, she breathed life into the city's forgotten tales, weaving a tapestry of connection that bound hearts together and illuminated the beauty of human spirit."
text2 = "As Lily poured her passion onto the canvas, her artwork became a beacon of creativity, drawing people from all walks of life to witness its transformation. Strangers became friends, sharing stories and laughter under the watchful gaze of the mural's characters. With each stroke of her brush, Lily discovered not only the power of art to inspire change but also the strength of community to uplift and support one another. As the final touches were made, the mural stood as a testament to resilience and unity, a symbol of hope that echoed through the streets of Ember Grove. And in the heart of it all, Lily found not only her voice as an artist but also her place in a world where human connection and creativity flourished, painting a brighter tomorrow for all who dared to dream."
text3 = "As Lily continued to paint, her mural grew into a living tapestry of the city's soul. Each stroke of her brush told a story—a tale of struggle, triumph, and the vibrant tapestry of life in Ember Grove. Passersby paused to admire her work, their eyes alight with wonder as they traced the contours of her creation."
text4 = "Yet, amidst the beauty she brought to the city streets, Lily grappled with doubts and fears of her own. Would her art truly make a difference? Could a single mural bridge the gaps that divided the people of Ember Grove? But with each passing day, as the community gathered around her masterpiece, Lily felt a glimmer of hope flicker within her—a belief that art had the power to heal, to unite, and to transform."

text1 = "In the land of Dracoria, where the mountains scraped the sky and the rivers ran with molten silver, there existed a tale as old as time itself—a tale of dragons. Majestic creatures of fire and fury, they soared through the heavens with wings of gold and scales of emerald, their roars echoing across the vast expanse of the realm. At the heart of Dracoria lay the Dragon's Keep, a fortress forged from the very bones of the earth, where the ancient dragons dwelled in peace and wisdom. Among them was Elandra, the guardian of the skies, whose wings blazed with the brilliance of a thousand suns. With her breath, she kindled the flames of creation, shaping the world with each beat of her mighty heart."
text2 = "But beyond the borders of Dracoria, darkness loomed—a shadowy force known as the Void, hungry for the destruction of all that was pure and true. Led by the enigmatic Shadow Lord, its armies marched relentlessly, seeking to enslave the dragons and bend their power to their will. In the face of this threat, Elandra called upon the bravest of souls—a young dragon rider named Aric, whose bond with his dragon companion, Ember, burned brighter than the fiercest flame. Together, they embarked on a quest to unite the scattered tribes of dragons, forging alliances and awakening ancient powers long thought lost to the sands of time."
text3 = "As they journeyed across Dracoria, they encountered trials and tribulations beyond imagination—fierce battles against monstrous beasts, treacherous journeys through unforgiving landscapes, and tests of courage that pushed them to the very brink of despair. Yet, with each challenge they faced, their bond grew stronger, their resolve unyielding in the face of adversity. At last, they stood before the gates of the Dragon's Keep, where Elandra awaited them with a wisdom as ancient as the stars. Together, they devised a plan to confront the Shadow Lord and his minions, to drive back the darkness and restore peace to the realm once more."
text4 = "With hearts ablaze and spirits unbroken, Aric and Ember soared into battle, their cries echoing through the mountains and valleys of Dracoria. And as the sun set on the horizon, casting its golden light upon the battlefield, they emerged victorious—a testament to the indomitable spirit of the dragons and the power of friendship, courage, and love to conquer even the darkest of foes. And so, in the land of Dracoria, the tale of dragons lived on—a tale of fire and fury, of triumph and sacrifice, and of the eternal bond between dragon and rider that would endure for all eternity."
#response = gen.model(respo, env["history"])
#respo = "A book cover to a story about a human excaping prison. Don't include words and keep the image clear."
#prompt = "Create the "
#gen.model(respo, env)
#respo = gen.intro_prompt(env)
#response = "Create an image of a disembodied head of a man, he is looking directly at the camera. He isn't scary, but rather a kind looking head. The head should go down to the top of the shoulders."
#response = gen.model(respo, env)
work = False
fails = 0
while work == False:
    try:
        response = gen.IMG_Prompt_model(text1)
        response['chapter'] = text1
        gen.img_model(response)

        #response = gen.IMG_Prompt_model(text2)
        response['chapter'] = text2
        gen.img_model(response)
        #response = gen.img_model(art)
        response['chapter'] = text3
        gen.img_model(response)
        response['chapter'] = text4
        gen.img_model(response)

        #print(response)
        work = True
    except Exception as e:
        print("trying again")
        work = False
        fails += 1
        if fails > 10:
            work = True
print(fails)
"Digital painting of a distinctly feminine green-eyed, white-furred tabaxi monk (with fluffy cheeks and a tuft on her head) with gradient shading, clean linework, vibrant palette, and stylized proportions. Wearing a simple green monk tunic and carrying a pack, [scenario]"