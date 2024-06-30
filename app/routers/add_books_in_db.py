from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter(tags=["add books data in the database"])

books_json = {
    "data": [
        {
            "id": "be86bc6e-d52e-4c46-86fe-76ce12fb99b2",
            "type": "book",
            "attributes": {
                "slug": "harry-potter-and-the-philosopher-s-stone",
                "author": "J. K. Rowling",
                "cover": "https://www.wizardingworld.com/images/products/books/UK/rectangle-1.jpg",
                "dedication": "For Jessica, who loves stories, for Anne, who loved them too, and for Di, who heard this one first",
                "pages": 223,
                "release_date": "1997-06-26",
                "summary": "Harry Potter has never even heard of Hogwarts when the letters start dropping on the doormat at number four, Privet Drive. Addressed in green ink on yellowish parchment with a purple seal, they are swiftly confiscated by his grisly aunt and uncle. Then, on Harry's eleventh birthday, a great beetle-eyed giant of a man called Rubeus Hagrid bursts in with some astonishing news: Harry Potter is a wizard, and he has a place at Hogwarts School of Witchcraft and Wizardry. An incredible adventure is about to begin!",
                "title": "Harry Potter and the Philosopher's Stone",
                "wiki": "https://harrypotter.fandom.com/wiki/Harry_Potter_and_the_Philosopher's_Stone",
            },
            "relationships": {
                "chapters": {
                    "data": [
                        {
                            "id": "b2088384-6b03-4741-ad18-34e9eb8834df",
                            "type": "chapter",
                        },
                        {
                            "id": "b3f51035-2869-4c3e-b6b9-92fce9bb481f",
                            "type": "chapter",
                        },
                        {
                            "id": "1e259859-67c7-4fa2-9cf4-12d748436534",
                            "type": "chapter",
                        },
                        {
                            "id": "e3576aa5-b585-4043-a185-e1da6b00e043",
                            "type": "chapter",
                        },
                        {
                            "id": "7447ccd6-0068-4475-a365-f53d36104f4b",
                            "type": "chapter",
                        },
                        {
                            "id": "193cae62-c8aa-4a52-b191-d97a4d825036",
                            "type": "chapter",
                        },
                        {
                            "id": "87e5cd9d-5290-4460-aa46-9ee402092b16",
                            "type": "chapter",
                        },
                        {
                            "id": "265b82e5-a8a1-4d5e-9cf7-551b4228bc59",
                            "type": "chapter",
                        },
                        {
                            "id": "6199520a-8327-4919-8477-4cf5af72efb4",
                            "type": "chapter",
                        },
                        {
                            "id": "15b56354-be5d-4830-8cc9-abbd976bd772",
                            "type": "chapter",
                        },
                        {
                            "id": "8b0fcdd8-d15a-4348-9ee5-7f504e8676f5",
                            "type": "chapter",
                        },
                        {
                            "id": "9b640bdb-5084-416c-b2a7-336d2c7cbc84",
                            "type": "chapter",
                        },
                        {
                            "id": "d51c5f61-9699-483d-9b5c-73dcac30777e",
                            "type": "chapter",
                        },
                        {
                            "id": "d5c2c90b-97df-452a-80d4-2d9dbc147b9d",
                            "type": "chapter",
                        },
                        {
                            "id": "d604437d-1425-47ed-a21d-f493d1361802",
                            "type": "chapter",
                        },
                        {
                            "id": "8672e622-c530-47f1-92c8-4be328598567",
                            "type": "chapter",
                        },
                        {
                            "id": "9d91e229-ba5b-410c-aa02-8d93122ade7c",
                            "type": "chapter",
                        },
                    ]
                }
            },
            "links": {"self": "/v1/books/be86bc6e-d52e-4c46-86fe-76ce12fb99b2"},
        },
        {
            "id": "96aa3ca0-c26a-4eb0-a1b6-c42b7dcff033",
            "type": "book",
            "attributes": {
                "slug": "harry-potter-and-the-chamber-of-secrets",
                "author": "J. K. Rowling",
                "cover": "https://www.wizardingworld.com/images/products/books/UK/rectangle-2.jpg",
                "dedication": "For Séan P. F. Harris, getaway driver and foul-weather friend",
                "pages": 251,
                "release_date": "1998-07-02",
                "summary": "Harry Potter's summer has included the worst birthday ever, doomy warnings from a house-elf called Dobby, and rescue from the Dursleys by his friend Ron Weasley in a magical flying car! Back at Hogwarts School of Witchcraft And Wizardry for his second year, Harry hears strange whispers echo through empty corridors – and then the attacks start. Students are found as though turned to stone... Dobby's sinister predictions seem to be coming true.",
                "title": "Harry Potter and the Chamber of Secrets",
                "wiki": "https://harrypotter.fandom.com/wiki/Harry_Potter_and_the_Chamber_of_Secrets",
            },
            "relationships": {
                "chapters": {
                    "data": [
                        {
                            "id": "70f50ea8-5aa0-4187-b236-1c4084ce1f47",
                            "type": "chapter",
                        },
                        {
                            "id": "e37441fa-99a4-4dfb-8264-a5ba3c4a4bd0",
                            "type": "chapter",
                        },
                        {
                            "id": "f6a656dc-79ca-45d2-adf2-38d364fdf603",
                            "type": "chapter",
                        },
                        {
                            "id": "67589bc3-90f0-4bbf-bc41-b51d0e97b526",
                            "type": "chapter",
                        },
                        {
                            "id": "6a6dcd5b-0bb1-40d0-a6f5-1877bf74a3f5",
                            "type": "chapter",
                        },
                        {
                            "id": "eb44faa2-05f3-4266-a0b7-d1929da2d24d",
                            "type": "chapter",
                        },
                        {
                            "id": "db9f1065-a8f2-4719-bd03-49fa69d1c887",
                            "type": "chapter",
                        },
                        {
                            "id": "4929303b-e682-4960-b77f-0e5890d63649",
                            "type": "chapter",
                        },
                        {
                            "id": "81279466-58e8-49c6-bcbd-bbfbf8dc6247",
                            "type": "chapter",
                        },
                        {
                            "id": "ee96bd1a-2776-4f1c-a6b6-cba04eabc925",
                            "type": "chapter",
                        },
                        {
                            "id": "a0e8052d-3269-47c3-a2f0-75646106d7fd",
                            "type": "chapter",
                        },
                        {
                            "id": "84df95b9-c1a2-41dc-8d1e-74b19e3546d4",
                            "type": "chapter",
                        },
                        {
                            "id": "e3936bf0-83c6-4a64-9991-86cac67356ae",
                            "type": "chapter",
                        },
                        {
                            "id": "bcfc88f0-9cbc-4ef0-9a32-d31e0cee25cc",
                            "type": "chapter",
                        },
                        {
                            "id": "c0c3d869-947a-475b-bd9e-2c56f88091a2",
                            "type": "chapter",
                        },
                        {
                            "id": "9f4b8b86-5a3f-4445-ac01-2f235ad9aca7",
                            "type": "chapter",
                        },
                        {
                            "id": "a9d3989c-8e8c-4efc-844e-b348cb04bbbb",
                            "type": "chapter",
                        },
                        {
                            "id": "a6a38d8a-4916-4fa9-83a3-4492d4511a60",
                            "type": "chapter",
                        },
                    ]
                }
            },
            "links": {"self": "/v1/books/96aa3ca0-c26a-4eb0-a1b6-c42b7dcff033"},
        },
        {
            "id": "39570ab3-08c2-42f0-b771-340739191cf3",
            "type": "book",
            "attributes": {
                "slug": "harry-potter-and-the-prisoner-of-azkaban",
                "author": "J. K. Rowling",
                "cover": "https://www.wizardingworld.com/images/products/books/UK/rectangle-3.jpg",
                "dedication": "To Jill Prewett and Aine Kiely, the Godmothers of Swing",
                "pages": 317,
                "release_date": "1999-07-08",
                "summary": "When the Knight Bus crashes through the darkness and screeches to a halt in front of him, it's the start of another far from ordinary year at Hogwarts for Harry Potter. Sirius Black, escaped mass-murderer and follower of Lord Voldemort, is on the run – and they say he is coming after Harry. In his first ever Divination class, Professor Trelawney sees an omen of death in Harry's tea leaves... But perhaps most terrifying of all are the Dementors patrolling the school grounds, with their soul-sucking kiss.",
                "title": "Harry Potter and the Prisoner of Azkaban",
                "wiki": "https://harrypotter.fandom.com/wiki/Harry_Potter_and_the_Prisoner_of_Azkaban",
            },
            "relationships": {
                "chapters": {
                    "data": [
                        {
                            "id": "48bd126d-b84b-42f8-abb6-075cb0c00e3b",
                            "type": "chapter",
                        },
                        {
                            "id": "177424ef-3573-4ea3-9177-d5a9496db83e",
                            "type": "chapter",
                        },
                        {
                            "id": "88cddf72-594b-4e31-974e-ab531e1b3c41",
                            "type": "chapter",
                        },
                        {
                            "id": "23d2d78d-3f35-41d8-a97e-365e8463d9e0",
                            "type": "chapter",
                        },
                        {
                            "id": "7410b164-b3bb-445e-bfc4-dc4de86224cb",
                            "type": "chapter",
                        },
                        {
                            "id": "81936c08-5a48-46ff-8f88-7b92a2e24221",
                            "type": "chapter",
                        },
                        {
                            "id": "1274e343-45fc-4da8-93da-e165318e4b4f",
                            "type": "chapter",
                        },
                        {
                            "id": "7602a029-de7d-4ea2-ad40-10e346994c0c",
                            "type": "chapter",
                        },
                        {
                            "id": "36833d91-b83c-49c2-9590-0308ab0c8d32",
                            "type": "chapter",
                        },
                        {
                            "id": "0a1a4953-2194-4a28-8cd0-809fb58f3dcc",
                            "type": "chapter",
                        },
                        {
                            "id": "6ad16335-b389-41b6-95bb-6b821d1e252a",
                            "type": "chapter",
                        },
                        {
                            "id": "27f44c6a-ccfc-455b-b34f-55863721a2e1",
                            "type": "chapter",
                        },
                        {
                            "id": "3f3fe16f-3dec-4d2c-bcd3-39b4a4343ffe",
                            "type": "chapter",
                        },
                        {
                            "id": "01cf23fa-eb7e-4f74-a534-dcd3ddbc7496",
                            "type": "chapter",
                        },
                        {
                            "id": "de29dc9e-f87e-415d-8541-e9ac201c563b",
                            "type": "chapter",
                        },
                        {
                            "id": "c597457c-5906-4700-942f-42a6f0e2501a",
                            "type": "chapter",
                        },
                        {
                            "id": "93625311-5085-465e-8dac-172a9724ecad",
                            "type": "chapter",
                        },
                        {
                            "id": "faadf0e3-4be5-4472-a7fc-9f4e7cf79c37",
                            "type": "chapter",
                        },
                        {
                            "id": "f9df4d0b-2d27-425f-8011-489bc740f757",
                            "type": "chapter",
                        },
                        {
                            "id": "ea2bf778-6474-4dcc-8da9-971e7c95759f",
                            "type": "chapter",
                        },
                        {
                            "id": "56f39594-6f98-4eb8-ace0-fcb78d9b057e",
                            "type": "chapter",
                        },
                        {
                            "id": "3e2b0faa-022a-401c-9429-644a9121fa15",
                            "type": "chapter",
                        },
                    ]
                }
            },
            "links": {"self": "/v1/books/39570ab3-08c2-42f0-b771-340739191cf3"},
        },
        {
            "id": "600ea74d-675b-42e1-af01-3370f4817060",
            "type": "book",
            "attributes": {
                "slug": "harry-potter-and-the-goblet-of-fire",
                "author": "J. K. Rowling",
                "cover": "https://www.wizardingworld.com/images/products/books/UK/rectangle-4.jpg",
                "dedication": "To Peter Rowling, in memory of Mr Ridley and to Susan Sladden, who helped Harry out of his cupboard",
                "pages": 636,
                "release_date": "2000-07-08",
                "summary": "The Triwizard Tournament is to be held at Hogwarts. Only wizards who are over seventeen are allowed to enter – but that doesn't stop Harry dreaming that he will win the competition. Then at Hallowe'en, when the Goblet of Fire makes its selection, Harry is amazed to find his name is one of those that the magical cup picks out. He will face death-defying tasks, dragons and Dark wizards, but with the help of his best friends, Ron and Hermione, he might just make it through – alive!",
                "title": "Harry Potter and the Goblet of Fire",
                "wiki": "https://harrypotter.fandom.com/wiki/Harry_Potter_and_the_Goblet_of_Fire",
            },
            "relationships": {
                "chapters": {
                    "data": [
                        {
                            "id": "709c0d6b-5c54-4468-a027-fd561bc4c9f2",
                            "type": "chapter",
                        },
                        {
                            "id": "380fa252-d856-400d-9759-52ddc5584323",
                            "type": "chapter",
                        },
                        {
                            "id": "43452482-cc4e-46ed-87b6-c9eddd26d9de",
                            "type": "chapter",
                        },
                        {
                            "id": "6d9c3b2d-ccd0-49db-8d94-269caf50c073",
                            "type": "chapter",
                        },
                        {
                            "id": "32f04fe9-af0b-4ceb-80ec-a58bab804c2d",
                            "type": "chapter",
                        },
                        {
                            "id": "28ba95aa-8ef3-46da-9bfc-ccd8db39b24b",
                            "type": "chapter",
                        },
                        {
                            "id": "51245fb5-5d82-4575-ba53-8987cf30480e",
                            "type": "chapter",
                        },
                        {
                            "id": "0c486f9c-ac56-48a1-9b95-8c1674fd6add",
                            "type": "chapter",
                        },
                        {
                            "id": "0d0d718e-66cf-419d-826f-0dea9c15073b",
                            "type": "chapter",
                        },
                        {
                            "id": "37f01e57-fd9f-4518-b0bd-47cf5b62b4a0",
                            "type": "chapter",
                        },
                        {
                            "id": "41457c67-cf5f-47b5-ac98-f2a08bb02d7d",
                            "type": "chapter",
                        },
                        {
                            "id": "857cb939-2152-467e-824d-826838dd520d",
                            "type": "chapter",
                        },
                        {
                            "id": "1cf1ceb8-7095-4e9b-ada3-2ee12595a65e",
                            "type": "chapter",
                        },
                        {
                            "id": "45e74d10-2c40-45f8-a9c0-01b3cf652835",
                            "type": "chapter",
                        },
                        {
                            "id": "6307f1c4-e0e4-46fa-b92b-068281bd6cf6",
                            "type": "chapter",
                        },
                        {
                            "id": "6b264058-d18f-404c-b40a-99e45322ceba",
                            "type": "chapter",
                        },
                        {
                            "id": "76598660-a92f-4ddd-902c-5075c00bcd46",
                            "type": "chapter",
                        },
                        {
                            "id": "abd03ab7-e62d-44e2-885f-ff35cc052150",
                            "type": "chapter",
                        },
                        {
                            "id": "c1a37ebd-0cac-4cac-a07e-9758090b8304",
                            "type": "chapter",
                        },
                        {
                            "id": "69f78c1e-0263-4e5f-acc6-e9d270ebdcee",
                            "type": "chapter",
                        },
                        {
                            "id": "c914c585-1b5d-4111-aaa0-5664fd17ff13",
                            "type": "chapter",
                        },
                        {
                            "id": "b1077651-c694-4b12-8b7d-f068d5a4ce5c",
                            "type": "chapter",
                        },
                        {
                            "id": "0fd6dfc7-4391-45d5-bd53-8ac97b25f797",
                            "type": "chapter",
                        },
                        {
                            "id": "76b65c12-39cd-4df0-b019-c3dfa3f9c6b9",
                            "type": "chapter",
                        },
                        {
                            "id": "03035c37-2bff-4519-b1af-550fb5b41b2d",
                            "type": "chapter",
                        },
                        {
                            "id": "2ccdc6df-8513-4a61-8f53-a0f1819e56aa",
                            "type": "chapter",
                        },
                        {
                            "id": "29fdbbde-2e4c-4f34-976f-6170644efab2",
                            "type": "chapter",
                        },
                        {
                            "id": "0cc001b9-c93a-4f9b-bd45-e37216db68df",
                            "type": "chapter",
                        },
                        {
                            "id": "aaec4ea9-9de5-46d1-958b-94d603edbbdb",
                            "type": "chapter",
                        },
                        {
                            "id": "042058a5-5268-40e0-b4d1-7f34142b5fbf",
                            "type": "chapter",
                        },
                        {
                            "id": "535872b4-8684-46f1-9139-a835a9c7b3d5",
                            "type": "chapter",
                        },
                        {
                            "id": "7a06ac70-72b2-49d9-ad41-cfa39b158ead",
                            "type": "chapter",
                        },
                        {
                            "id": "02f8465b-e3a9-4a94-8b0b-2f731d06ce3f",
                            "type": "chapter",
                        },
                        {
                            "id": "7da683ef-8738-4aa7-8136-646c4b62fb07",
                            "type": "chapter",
                        },
                        {
                            "id": "93f3d162-6178-4987-9fc0-c405f9184bf4",
                            "type": "chapter",
                        },
                        {
                            "id": "db2cfd0b-0006-40f8-9c01-7535d987c383",
                            "type": "chapter",
                        },
                        {
                            "id": "2c984bb6-dbc2-41f7-8f5f-150db843c995",
                            "type": "chapter",
                        },
                    ]
                }
            },
            "links": {"self": "/v1/books/600ea74d-675b-42e1-af01-3370f4817060"},
        },
        {
            "id": "d04e8b0b-761c-4ef4-a68c-6503f1ca1d06",
            "type": "book",
            "attributes": {
                "slug": "harry-potter-and-the-order-of-the-phoenix",
                "author": "J. K. Rowling",
                "cover": "https://www.wizardingworld.com/images/products/books/UK/rectangle-5.jpg",
                "dedication": "To Neil, Jessica and David, who make my world magical",
                "pages": 766,
                "release_date": "2003-06-21",
                "summary": "Dark times have come to Hogwarts. After the Dementors' attack on his cousin Dudley, Harry Potter knows that Voldemort will stop at nothing to find him. There are many who deny the Dark Lord's return, but Harry is not alone: a secret Order gathers at Grimmauld Place to fight against the Dark forces. Harry must allow Professor Snape to teach him how to protect himself from Voldemort's savage assaults on his mind. But they are growing stronger by the day and Harry is running out of time.",
                "title": "Harry Potter and the Order of the Phoenix",
                "wiki": "https://harrypotter.fandom.com/wiki/Harry_Potter_and_the_Order_of_the_Phoenix",
            },
            "relationships": {
                "chapters": {
                    "data": [
                        {
                            "id": "95a8471b-d606-422f-94c9-6e183d05654e",
                            "type": "chapter",
                        },
                        {
                            "id": "e17b8f80-506f-440b-a543-cd655b25c10d",
                            "type": "chapter",
                        },
                        {
                            "id": "eb6c3368-c403-4716-906b-5118aca84661",
                            "type": "chapter",
                        },
                        {
                            "id": "5f152ac0-3066-421b-a88e-a882077ef6ee",
                            "type": "chapter",
                        },
                        {
                            "id": "46246fe9-6495-46b2-a896-05b9d04d5ce1",
                            "type": "chapter",
                        },
                        {
                            "id": "d8663557-2be0-4e2c-9d2b-06697defbcc0",
                            "type": "chapter",
                        },
                        {
                            "id": "3715a1eb-b9f2-4972-8db9-2ef6f3e5d102",
                            "type": "chapter",
                        },
                        {
                            "id": "85fbe9e3-1eb3-4f67-ac35-1e03d0d8e2ad",
                            "type": "chapter",
                        },
                        {
                            "id": "a63e31cb-9951-4454-93ed-ff2e93d4b792",
                            "type": "chapter",
                        },
                        {
                            "id": "b0143ea4-9a6b-4e67-9cae-406a7d375e07",
                            "type": "chapter",
                        },
                        {
                            "id": "16ece107-1466-4add-9626-743adcd0d9f7",
                            "type": "chapter",
                        },
                        {
                            "id": "ba748327-42fd-45f4-b127-db12f3871a39",
                            "type": "chapter",
                        },
                        {
                            "id": "3b007486-9427-4c46-9e23-c0359db01d47",
                            "type": "chapter",
                        },
                        {
                            "id": "aed51cc5-86c6-4b7c-a882-f8419645088a",
                            "type": "chapter",
                        },
                        {
                            "id": "037d5e0c-93ac-40b2-ba65-225f4c54290e",
                            "type": "chapter",
                        },
                        {
                            "id": "3f31b25a-8b5d-4164-bda3-aa1255725f39",
                            "type": "chapter",
                        },
                        {
                            "id": "8ce933ef-6127-42ad-a481-e26f08f82117",
                            "type": "chapter",
                        },
                        {
                            "id": "3086e854-59c9-46ed-a01c-56fbb06a7740",
                            "type": "chapter",
                        },
                        {
                            "id": "7810a0d9-5a5b-44cf-8d70-33cd7f40e101",
                            "type": "chapter",
                        },
                        {
                            "id": "67cb61f7-e7a6-4edf-9ffb-9082671421aa",
                            "type": "chapter",
                        },
                        {
                            "id": "e94877e6-1f11-4350-97ec-dfbfa064de3f",
                            "type": "chapter",
                        },
                        {
                            "id": "519d2849-781c-4e30-bbc1-4261a6e25d6d",
                            "type": "chapter",
                        },
                        {
                            "id": "74487bcf-ab96-4ec6-a4a6-43c69b286f76",
                            "type": "chapter",
                        },
                        {
                            "id": "bebf26e6-52fa-4c30-8d10-23d09dec0ca4",
                            "type": "chapter",
                        },
                        {
                            "id": "3ed0cffc-feb4-41f4-96fa-f07801be7b0f",
                            "type": "chapter",
                        },
                        {
                            "id": "2bffa35b-3bd7-4fb0-a36f-0c5f2b10a27f",
                            "type": "chapter",
                        },
                        {
                            "id": "d417fa67-6552-4549-a2c3-0d6ffb362b5e",
                            "type": "chapter",
                        },
                        {
                            "id": "61afdee7-8c7e-41cf-bcc0-03e21babcc96",
                            "type": "chapter",
                        },
                        {
                            "id": "ab2616fb-1f32-46f3-ba56-31c289dbc0bd",
                            "type": "chapter",
                        },
                        {
                            "id": "2979b38f-999c-41de-af5d-fdfd49b3b8ad",
                            "type": "chapter",
                        },
                        {
                            "id": "d476ef81-9d0e-4e7c-a97b-f32ac7ccefba",
                            "type": "chapter",
                        },
                        {
                            "id": "24be6021-2ac2-4a3d-bbf0-167bdde3cc43",
                            "type": "chapter",
                        },
                        {
                            "id": "3d91f38d-4ebf-4105-a95c-4ccfc8264277",
                            "type": "chapter",
                        },
                        {
                            "id": "2678823f-864e-4472-b29c-1f26c410e73a",
                            "type": "chapter",
                        },
                        {
                            "id": "e3b3bd69-41f6-489c-ac17-394ea32e2d9d",
                            "type": "chapter",
                        },
                        {
                            "id": "f5863895-2ee4-43e8-b591-02ad32312e55",
                            "type": "chapter",
                        },
                        {
                            "id": "c55f412e-5d8f-4cce-83e7-7192748094e5",
                            "type": "chapter",
                        },
                        {
                            "id": "c2dfd7f2-739e-4095-a99b-c2904eb7f899",
                            "type": "chapter",
                        },
                    ]
                }
            },
            "links": {"self": "/v1/books/d04e8b0b-761c-4ef4-a68c-6503f1ca1d06"},
        },
        {
            "id": "84b0a42e-40b8-4b5d-a935-f52f9c231351",
            "type": "book",
            "attributes": {
                "slug": "harry-potter-and-the-half-blood-prince",
                "author": "J. K. Rowling",
                "cover": "https://www.wizardingworld.com/images/products/books/UK/rectangle-6.jpg",
                "dedication": "To Mackenzie, My beautiful daughter, I dedicate Her ink-and-paper twin.",
                "pages": 607,
                "release_date": "2005-07-16",
                "summary": "When Dumbledore arrives at Privet Drive one summer night to collect Harry Potter, his wand hand is blackened and shrivelled, but he does not reveal why. Secrets and suspicion are spreading through the wizarding world, and Hogwarts itself is not safe. Harry is convinced that Malfoy bears the Dark Mark: there is a Death Eater amongst them. Harry will need powerful magic and true friends as he explores Voldemort's darkest secrets, and Dumbledore prepares him to face his destiny.",
                "title": "Harry Potter and the Half-Blood Prince",
                "wiki": "https://harrypotter.fandom.com/wiki/Harry_Potter_and_the_Half-Blood_Prince",
            },
            "relationships": {
                "chapters": {
                    "data": [
                        {
                            "id": "6009e217-c37f-4a46-8121-5a66fb265334",
                            "type": "chapter",
                        },
                        {
                            "id": "b5c0df05-c79f-4864-9439-db92829b876a",
                            "type": "chapter",
                        },
                        {
                            "id": "7d792f34-e3bc-4e01-9010-353bf11408d2",
                            "type": "chapter",
                        },
                        {
                            "id": "e4fc42da-a9ef-4262-9055-6e48bca1b7ea",
                            "type": "chapter",
                        },
                        {
                            "id": "8d45323a-f8f6-4799-9e0f-740ff7f2834f",
                            "type": "chapter",
                        },
                        {
                            "id": "369a114d-18a3-4993-bb0d-28d2f7c6d41c",
                            "type": "chapter",
                        },
                        {
                            "id": "6dc1a890-1063-4deb-92be-79dcfe75507c",
                            "type": "chapter",
                        },
                        {
                            "id": "343dbfcd-ec86-4ce2-a08f-ea91ebbfcb9d",
                            "type": "chapter",
                        },
                        {
                            "id": "7ae79c02-bf4a-427d-9bef-8e6980767ff4",
                            "type": "chapter",
                        },
                        {
                            "id": "b9aa05c5-a575-4f2d-bf18-dcb6146a1d20",
                            "type": "chapter",
                        },
                        {
                            "id": "3a7874b6-006e-4a3a-a3f5-3c61ef892530",
                            "type": "chapter",
                        },
                        {
                            "id": "0e798c58-3ff1-4412-92c6-2995d4e2eb18",
                            "type": "chapter",
                        },
                        {
                            "id": "c1d26357-e053-4b08-8b6d-207ffd89e5f1",
                            "type": "chapter",
                        },
                        {
                            "id": "20c29df5-1845-4581-86f6-20a309721ea4",
                            "type": "chapter",
                        },
                        {
                            "id": "76be6506-48f1-44cf-8ba7-ddd008ca50bd",
                            "type": "chapter",
                        },
                        {
                            "id": "678070ef-6a3a-478f-a8b2-2389b1bc786e",
                            "type": "chapter",
                        },
                        {
                            "id": "6aed8858-a0f4-44ca-99c6-6e98676ac8be",
                            "type": "chapter",
                        },
                        {
                            "id": "e2f5a946-87b4-4f07-a9e3-8586e8f6e108",
                            "type": "chapter",
                        },
                        {
                            "id": "be7849dc-3dd9-4454-994e-9ad68f17c6a6",
                            "type": "chapter",
                        },
                        {
                            "id": "c6619f94-4fe5-49ee-80dc-ddb617ffd45f",
                            "type": "chapter",
                        },
                        {
                            "id": "2f05a8de-5ade-4d1b-a259-6b0cab95714a",
                            "type": "chapter",
                        },
                        {
                            "id": "42e0ef09-684f-47b4-b52d-38946d50d6eb",
                            "type": "chapter",
                        },
                        {
                            "id": "a1d7b5a2-1395-49ca-98f1-f7ae18516f39",
                            "type": "chapter",
                        },
                        {
                            "id": "eedcc50e-be86-4a9e-b4db-2becfc2f0366",
                            "type": "chapter",
                        },
                        {
                            "id": "9afa1a4c-7a79-4cd8-964f-992f4ab47c42",
                            "type": "chapter",
                        },
                        {
                            "id": "6ebfe660-2f5f-4118-a52c-cba102ef60fe",
                            "type": "chapter",
                        },
                        {
                            "id": "c44d0dec-61f6-4b0e-8a12-adcd80935e3a",
                            "type": "chapter",
                        },
                        {
                            "id": "dc0bb547-edd0-434a-85de-6171390c055d",
                            "type": "chapter",
                        },
                        {
                            "id": "b42a572e-0e1a-404b-9a1f-f1eb294d726b",
                            "type": "chapter",
                        },
                        {
                            "id": "76e2f781-2979-4184-a628-34c6fdc9d177",
                            "type": "chapter",
                        },
                    ]
                }
            },
            "links": {"self": "/v1/books/84b0a42e-40b8-4b5d-a935-f52f9c231351"},
        },
        {
            "id": "4a048179-15d0-4d30-8bab-4138f6c1d422",
            "type": "book",
            "attributes": {
                "slug": "harry-potter-and-the-deathly-hallows",
                "author": "J. K. Rowling",
                "cover": "https://www.wizardingworld.com/images/products/books/UK/rectangle-7.jpg",
                "dedication": "To Neil, To Jessica, To David, To Kenzie, To Di, To Anne, And to You If you have stuck with Harry until the very end.",
                "pages": 610,
                "release_date": "2007-07-21",
                "summary": "As he climbs into the sidecar of Hagrid's motorbike and takes to the skies, leaving Privet Drive for the last time, Harry Potter knows that Lord Voldemort and the Death Eaters are not far behind. The protective charm that has kept Harry safe until now is broken, but he cannot keep hiding. The Dark Lord is breathing fear into everything Harry loves, and to stop him Harry will have to find and destroy the remaining Horcruxes. The final battle must begin – Harry must stand and face his enemy.",
                "title": "Harry Potter and the Deathly Hallows",
                "wiki": "https://harrypotter.fandom.com/wiki/Harry_Potter_and_the_Deathly_Hallows",
            },
            "relationships": {
                "chapters": {
                    "data": [
                        {
                            "id": "6ce5f261-6606-49a0-b440-e2b84d860861",
                            "type": "chapter",
                        },
                        {
                            "id": "a42aab40-d9f1-4344-a33e-030ab8b3428f",
                            "type": "chapter",
                        },
                        {
                            "id": "a3c94430-abeb-404f-b2e3-9549bbb4126f",
                            "type": "chapter",
                        },
                        {
                            "id": "0c01690b-a38d-4a7f-a59c-347621a22ecb",
                            "type": "chapter",
                        },
                        {
                            "id": "94ad5a65-033c-490c-b747-a3fff3cc0db7",
                            "type": "chapter",
                        },
                        {
                            "id": "7cbe6f1b-9347-428b-9f1e-c5670d8dd132",
                            "type": "chapter",
                        },
                        {
                            "id": "f3ca0beb-e4f6-40af-894d-bc1ae84d0827",
                            "type": "chapter",
                        },
                        {
                            "id": "6850edc5-36cc-476a-b927-ca234a91c3ea",
                            "type": "chapter",
                        },
                        {
                            "id": "8902ef22-c0fe-43c3-8935-355041b10042",
                            "type": "chapter",
                        },
                        {
                            "id": "ab996843-11dd-4417-a717-3f5816b40bd0",
                            "type": "chapter",
                        },
                        {
                            "id": "a0a520bc-b9c0-419f-8dd2-be1dcf80ee88",
                            "type": "chapter",
                        },
                        {
                            "id": "51840da1-c980-4146-a4b6-d4867c81c4ef",
                            "type": "chapter",
                        },
                        {
                            "id": "0fccbd05-1af9-4a45-8e86-6eaf8ffd90d3",
                            "type": "chapter",
                        },
                        {
                            "id": "4ddb774e-ecf6-499e-b490-4d9e59102e05",
                            "type": "chapter",
                        },
                        {
                            "id": "857f4ac9-399a-48b7-a2a6-5a9b1e741e45",
                            "type": "chapter",
                        },
                        {
                            "id": "4e079109-1495-4627-92b6-9b4635695e22",
                            "type": "chapter",
                        },
                        {
                            "id": "5cf0df0a-59f5-482a-a2f4-241e5b3765ac",
                            "type": "chapter",
                        },
                        {
                            "id": "ab1385ff-0bc6-45e8-bc5b-37aeb584d5ee",
                            "type": "chapter",
                        },
                        {
                            "id": "e3de8936-14c9-43e5-a271-72a77c6ddbd9",
                            "type": "chapter",
                        },
                        {
                            "id": "d2df4ede-4872-415f-84aa-c0c74e165c93",
                            "type": "chapter",
                        },
                        {
                            "id": "f136e82d-7261-4d3d-8eb6-2b66b0dc914b",
                            "type": "chapter",
                        },
                        {
                            "id": "9930c1a8-3269-4cca-aba9-a53294d12a76",
                            "type": "chapter",
                        },
                        {
                            "id": "e0f43452-1fcf-46d1-98fe-dbe665b0f8e7",
                            "type": "chapter",
                        },
                        {
                            "id": "ef55f840-2590-4e3b-bdd7-2a1f8b4b807a",
                            "type": "chapter",
                        },
                        {
                            "id": "e739e2b8-2b0e-45b4-9f02-e308b0742ffb",
                            "type": "chapter",
                        },
                        {
                            "id": "8e05f091-977d-4aeb-abd2-4e5e064554a1",
                            "type": "chapter",
                        },
                        {
                            "id": "1b54a0fa-cb7b-467c-b4a4-d5590f02eb6d",
                            "type": "chapter",
                        },
                        {
                            "id": "f9ef12de-95d9-48f3-a685-122859202bdd",
                            "type": "chapter",
                        },
                        {
                            "id": "f06608a7-7a9e-40c2-aa55-7dc4467494d1",
                            "type": "chapter",
                        },
                        {
                            "id": "932e5c6a-006e-4fcc-9ad4-9948318b660e",
                            "type": "chapter",
                        },
                        {
                            "id": "5e302d3b-ec71-4545-9de0-7a76afe198d0",
                            "type": "chapter",
                        },
                        {
                            "id": "d1bc1024-167c-4ef1-abc6-1ad21ab66f19",
                            "type": "chapter",
                        },
                        {
                            "id": "738d8a73-6637-4d15-a411-677da4d2c355",
                            "type": "chapter",
                        },
                        {
                            "id": "7cb3fc97-ba08-4690-8c68-d59c586bc4e7",
                            "type": "chapter",
                        },
                        {
                            "id": "25a2848f-0ab5-4031-b2d1-91669d219607",
                            "type": "chapter",
                        },
                        {
                            "id": "d7fd7b67-993b-4c41-9e5d-0aa9273d7de1",
                            "type": "chapter",
                        },
                        {
                            "id": "36011857-c5cb-42da-b7e0-8698512ca326",
                            "type": "chapter",
                        },
                    ]
                }
            },
            "links": {"self": "/v1/books/4a048179-15d0-4d30-8bab-4138f6c1d422"},
        },
    ],
    "meta": {
        "pagination": {"current": 1, "records": 7},
        "copyright": "Copyright © Potter DB 2024",
        "generated_at": "2024-02-20T23:11:46.690Z",
    },
    "links": {
        "self": "https://api.potterdb.com/v1/books",
        "current": "https://api.potterdb.com/v1/books?page[number]=1",
    },
}


@router.get("/add_books")
def add_books_in_db(db: Session = Depends(get_db)):
    for book in books_json["data"]:
        book_id = book["id"]
        title = book["attributes"]["title"]
        author = book["attributes"]["author"]
        cover = book["attributes"]["cover"]
        release_date = book["attributes"]["release_date"]
        total_chapters = len(book["relationships"]["chapters"]["data"])
        pages = book["attributes"]["pages"]
        summary = book["attributes"]["summary"]
        wiki = book["attributes"]["wiki"]

        row = models.Book(
            book_id=book_id,
            title=title,
            author=author,
            cover=cover,
            release_date=release_date,
            total_chapters=total_chapters,
            pages=pages,
            summary=summary,
            wiki=wiki,
        )

        db.add(row)
        db.commit()

    return {"message": "successfully added books"}
