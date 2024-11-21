from django.core.management.base import BaseCommand
from ArtI.models import Creator, Creation, Category


class Command(BaseCommand):
    help = "Seed the database with sample data"

    def handle(self, *args, **kwargs):
        # Create Categories
        categories = [
            Category(style="Underwater Art"),
            Category(style="Garden Art"),
            Category(style="Geometric Art"),
            Category(style="Steampunk Art"),
        ]
        Category.objects.bulk_create(categories)
        self.stdout.write("Categories created!")

        # Create Creators
        creators = [
            Creator(
                name="Aquaman",
                biography="Who lives in a pineapple at the bottom of the sea !?",
                logo="",
                created_at="2023-01-01",
            ),
            Creator(
                name="Willy Gardener",
                biography="He's the root cause we are digging AI art.",
                logo="",
                created_at="2023-02-01",
            ),
            Creator(
                name="G.O. Metery",
                biography="To be fair and square he is straight up the best",
                logo="",
                created_at="2023-02-01",
            ),
            Creator(
                name="Vapor Rebel",
                biography="Let off steam !",
                logo="",
                created_at="2023-02-01",
            ),
        ]
        Creator.objects.bulk_create(creators)
        self.stdout.write("Creators created!")

        # Create Creations
        creations = [
            Creation(
                title="Atlantis 1",
                prompt="Beneath the glistening waters lies the mysterious lost city of Atlantis. A surreal underwater civilization teeming with ancient ruins and mystical creatures, captured in a stunning digital painting. The sunken palaces are adorned with intricate carvings and shimmering treasures, while ethereal light filters through the water, casting an otherworldly glow. This masterpiece of a depiction immerses viewers in a mesmerizing world of fantasy and wonder.",
                description="Une plage sous l'océan !? C'est du génie !",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/3c251e20-fa9d-4615-bb22-d0197cfc3a2a/Leonardo_Phoenix_Beneath_the_glistening_waters_lies_the_myster_3.jpg",
                artist=creators[0],
            ),
            Creation(
                title="Atlantis 2",
                prompt="Beneath the glistening waters lies the mysterious lost city of Atlantis. A surreal underwater civilization teeming with ancient ruins and mystical creatures, captured in a stunning digital painting. The sunken palaces are adorned with intricate carvings and shimmering treasures, while ethereal light filters through the water, casting an otherworldly glow. This masterpiece of a depiction immerses viewers in a mesmerizing world of fantasy and wonder.",
                description="Nan mais en vrai, sous l'eau y a de l'eau aussi, en soit je vois pas le problème",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/6fb89072-be21-4def-85c4-5d56fbe73dba/Leonardo_Phoenix_Beneath_the_glistening_waters_lies_the_myster_3.jpg?w=512",
                artist=creators[0],
            ),
            Creation(
                title="Atlantis 3",
                prompt="Beneath the glistening waters lies the mysterious lost city of Atlantis. A surreal underwater civilization teeming with ancient ruins and mystical creatures, captured in a stunning digital painting. The sunken palaces are adorned with intricate carvings and shimmering treasures, while ethereal light filters through the water, casting an otherworldly glow. This masterpiece of a depiction immerses viewers in a mesmerizing world of fantasy and wonder.",
                description="Et puis, si il n'avait pas de bassin sous l'eau comment ils prendraient leurs bains les atlantes ? Bah voilà ! C'est cohérent.",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/6fb89072-be21-4def-85c4-5d56fbe73dba/Leonardo_Phoenix_Beneath_the_glistening_waters_lies_the_myster_0.jpg?w=512",
                artist=creators[0],
            ),
            Creation(
                title="Garden 1",
                prompt="A tranquil, expansive zen garden labyrinth sprawls before the viewer, captured from a bird's eye view. The intricate pathways wind through meticulously arranged rocks and delicate vegetation, creating a harmonious and contemplative landscape. Each detail is bathed in soft, natural light, enhancing the serene atmosphere of the scene. The image, whether portrayed through a painting or photograph, exudes a sense of peace and balance, inviting viewers to immerse themselves in its beauty.",
                description="Les labyrinthes sans entrée ça a l'avantage qu'on à peu de risque de s'y perdre",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/c1f75869-b81c-418a-9c51-7d35fbeecc4f/Leonardo_Phoenix_From_a_birdseye_view_a_intricate_maze_sprawls_3.jpg?w=512",
                artist=creators[1],
            ),
            Creation(
                title="Garden 2",
                prompt="A tranquil, expansive zen garden labyrinth sprawls before the viewer, captured from a bird's eye view. The intricate pathways wind through meticulously arranged rocks and delicate vegetation, creating a harmonious and contemplative landscape. Each detail is bathed in soft, natural light, enhancing the serene atmosphere of the scene. The image, whether portrayed through a painting or photograph, exudes a sense of peace and balance, inviting viewers to immerse themselves in its beauty.",
                description="Je n'ai étonnement rien à redire",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/270ae11e-fb29-4906-ba9f-26945e77e858/Leonardo_Phoenix_A_tranquil_expansive_zen_garden_labyrinth_spr_1.jpg?w=512",
                artist=creators[1],
            ),
            Creation(
                title="Garden 3",
                prompt="A tranquil, expansive zen garden labyrinth sprawls before the viewer, captured from a bird's eye view. The intricate pathways wind through meticulously arranged rocks and delicate vegetation, creating a harmonious and contemplative landscape. Each detail is bathed in soft, natural light, enhancing the serene atmosphere of the scene. The image, whether portrayed through a painting or photograph, exudes a sense of peace and balance, inviting viewers to immerse themselves in its beauty.",
                description="On est pas sorti",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/270ae11e-fb29-4906-ba9f-26945e77e858/Leonardo_Phoenix_A_tranquil_expansive_zen_garden_labyrinth_spr_0.jpg?w=512",
                artist=creators[1],
            ),
            Creation(
                title="Geometry 1",
                prompt="a highly detailed, hyper-realistic, lush, and surreal ray-traced render of a Voronoi diagram background for a website, featuring a 3D model illuminated by a vibrant, exaggerated ring light, set against a rich, gradient-like backdrop comprising three nuanced shades of dark grey, from charcoal to anthracite, alongside platinum and steel blue hues, evoking a sense of futuristic sophistication, with a crisp, pristine, and unreal engine quality, exuding an atmosphere of excitement and wonder, every intricate detail painstakingly rendered to perfection, with a keen focus on textures, reflections, and subtle lighting effects that elevate the overall sense of realism and visual drama.",
                description="C'est pas mal mais si tu pouvais éviter d'écrire le prompt sur le tableau ça serait pas mal",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/d9054aec-287f-45a1-ac8e-ebe4455590c0/Leonardo_Phoenix_a_highly_detailed_hyperrealistic_lush_and_sur_1.jpg?w=512",
                artist=creators[2],
            ),
            Creation(
                title="Geometry 2",
                prompt="a highly detailed, hyper-realistic, lush, and surreal ray-traced render of a Voronoi diagram background for a website, featuring a 3D model illuminated by a vibrant, exaggerated ring light, set against a rich, gradient-like backdrop comprising three nuanced shades of dark grey, from charcoal to anthracite, alongside platinum and steel blue hues, evoking a sense of futuristic sophistication, with a crisp, pristine, and unreal engine quality, exuding an atmosphere of excitement and wonder, every intricate detail painstakingly rendered to perfection, with a keen focus on textures, reflections, and subtle lighting effects that elevate the overall sense of realism and visual drama.",
                description="Nan mais vraiment, arrête d'écrire",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/d9054aec-287f-45a1-ac8e-ebe4455590c0/Leonardo_Phoenix_a_highly_detailed_hyperrealistic_lush_and_sur_2.jpg?w=512",
                artist=creators[2],
            ),
            Creation(
                title="Geometry 3",
                prompt="a highly detailed, hyper-realistic, lush, and surreal ray-traced render of a Voronoi diagram background for a website, featuring a 3D model illuminated by a vibrant, exaggerated ring light, set against a rich, gradient-like backdrop comprising three nuanced shades of dark grey, from charcoal to anthracite, alongside platinum and steel blue hues, evoking a sense of futuristic sophistication, with a crisp, pristine, and unreal engine quality, exuding an atmosphere of excitement and wonder, every intricate detail painstakingly rendered to perfection, with a keen focus on textures, reflections, and subtle lighting effects that elevate the overall sense of realism and visual drama.",
                description="Le concept de faire de l'art graphique c'est de ne pas avoir à écrire ce que tu peint en fait.",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/d9054aec-287f-45a1-ac8e-ebe4455590c0/Leonardo_Phoenix_a_highly_detailed_hyperrealistic_lush_and_sur_0.jpg?w=512",
                artist=creators[2],
            ),
            Creation(
                title="Steampunk 1",
                prompt="A sprawling steampunk metropolis with intricately interconnected buildings, bridges, and clockwork machinery, evoking the impossible geometry and paradoxical structures reminiscent of Mauritz Cornelis Escher's iconic paintings, set against a warm, golden-brown backdrop of worn, aged copper and bronze, with gleaming brass accents and intricate etchings, amidst wispy clouds of steam and smoke, where Gothic spires and grand, curved glass domes converge with labyrinthine alleys and cobblestone streets, illuminated by flickering gas lamps and soft, ethereal luminescence emanating from the clockwork contraptions, as if the very fabric of reality has been reshaped by the ingenious hands of steampunk innovators.",
                description="Une incroyable vue depuis les hauteurs de cette fantastique ville.",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/80206b0f-dfb2-4710-909a-3170c4a5eaed/Leonardo_Phoenix_A_sprawling_steampunk_metropolis_with_intrica_3.jpg",
                artist=creators[3],
            ),
            Creation(
                title="Steampunk 2",
                prompt="A sprawling steampunk metropolis with intricately interconnected buildings, bridges, and clockwork machinery, evoking the impossible geometry and paradoxical structures reminiscent of Mauritz Cornelis Escher's iconic paintings, set against a warm, golden-brown backdrop of worn, aged copper and bronze, with gleaming brass accents and intricate etchings, amidst wispy clouds of steam and smoke, where Gothic spires and grand, curved glass domes converge with labyrinthine alleys and cobblestone streets, illuminated by flickering gas lamps and soft, ethereal luminescence emanating from the clockwork contraptions, as if the very fabric of reality has been reshaped by the ingenious hands of steampunk innovators.",
                description="Une incroyable vue depuis les hauteurs de cette fantastique ville.",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/94eac8f6-74ed-4c54-942e-1cc2acbe4cee/Leonardo_Phoenix_A_sprawling_steampunk_metropolis_with_intrica_3.jpg?w=512",
                artist=creators[3],
            ),
            Creation(
                title="Steampunk 3",
                prompt="A sprawling steampunk metropolis with intricately interconnected buildings, bridges, and clockwork machinery, evoking the impossible geometry and paradoxical structures reminiscent of Mauritz Cornelis Escher's iconic paintings, set against a warm, golden-brown backdrop of worn, aged copper and bronze, with gleaming brass accents and intricate etchings, amidst wispy clouds of steam and smoke, where Gothic spires and grand, curved glass domes converge with labyrinthine alleys and cobblestone streets, illuminated by flickering gas lamps and soft, ethereal luminescence emanating from the clockwork contraptions, as if the very fabric of reality has been reshaped by the ingenious hands of steampunk innovators.",
                description="Une incroyable vue depuis les hauteurs de cette fantastique ville.",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/94eac8f6-74ed-4c54-942e-1cc2acbe4cee/Leonardo_Phoenix_A_sprawling_steampunk_metropolis_with_intrica_2.jpg",
                artist=creators[3],
            ),
            Creation(
                title="Steampunk 4",
                prompt="A sprawling steampunk metropolis with intricately interconnected buildings, bridges, and clockwork machinery, evoking the impossible geometry and paradoxical structures reminiscent of Mauritz Cornelis Escher's iconic paintings, set against a warm, golden-brown backdrop of worn, aged copper and bronze, with gleaming brass accents and intricate etchings, amidst wispy clouds of steam and smoke, where Gothic spires and grand, curved glass domes converge with labyrinthine alleys and cobblestone streets, illuminated by flickering gas lamps and soft, ethereal luminescence emanating from the clockwork contraptions, as if the very fabric of reality has been reshaped by the ingenious hands of steampunk innovators.",
                description="Une incroyable vue depuis les hauteurs de cette fantastique ville.",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/80206b0f-dfb2-4710-909a-3170c4a5eaed/Leonardo_Phoenix_A_sprawling_steampunk_metropolis_with_intrica_1.jpg",
                artist=creators[3],
            ),
            Creation(
                title="Steampunk 5",
                prompt="A sprawling steampunk metropolis with intricately interconnected buildings, bridges, and clockwork machinery, evoking the impossible geometry and paradoxical structures reminiscent of Mauritz Cornelis Escher's iconic paintings, set against a warm, golden-brown backdrop of worn, aged copper and bronze, with gleaming brass accents and intricate etchings, amidst wispy clouds of steam and smoke, where Gothic spires and grand, curved glass domes converge with labyrinthine alleys and cobblestone streets, illuminated by flickering gas lamps and soft, ethereal luminescence emanating from the clockwork contraptions, as if the very fabric of reality has been reshaped by the ingenious hands of steampunk innovators.",
                description="Une incroyable vue depuis les hauteurs de cette fantastique ville.",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/94eac8f6-74ed-4c54-942e-1cc2acbe4cee/Leonardo_Phoenix_A_sprawling_steampunk_metropolis_with_intrica_0.jpg?w=512",
                artist=creators[3],
            ),
            Creation(
                title="Steampunk 6",
                prompt="A sprawling steampunk metropolis with intricately interconnected buildings, bridges, and clockwork machinery, evoking the impossible geometry and paradoxical structures reminiscent of Mauritz Cornelis Escher's iconic paintings, set against a warm, golden-brown backdrop of worn, aged copper and bronze, with gleaming brass accents and intricate etchings, amidst wispy clouds of steam and smoke, where Gothic spires and grand, curved glass domes converge with labyrinthine alleys and cobblestone streets, illuminated by flickering gas lamps and soft, ethereal luminescence emanating from the clockwork contraptions, as if the very fabric of reality has been reshaped by the ingenious hands of steampunk innovators.",
                description="Une incroyable vue depuis les hauteurs de cette fantastique ville.",
                link="https://cdn.leonardo.ai/users/d6d58f8b-01eb-4d1f-823c-1c72755a7599/generations/4c3edf88-75cf-4128-8b4f-31533b25e021/Leonardo_Phoenix_A_sprawling_steampunk_metropolis_with_intrica_0.jpg",
                artist=creators[3],
            ),
        ]
        Creation.objects.bulk_create(creations)
        self.stdout.write("Creations created!")
