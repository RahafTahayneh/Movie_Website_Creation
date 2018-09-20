import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        " A Story of a boy and his toys that come to life",
                        "https://www.google.com/imgres?imgurl=http://www.gstatic.com/tv/thumb/v22vodart/17420/p17420_v_v8_an.jpg&imgrefurl=http://google.com/search?tbm%3Disch%26q%3DToy%2BStory&h=1440&w=960&tbnid=dh374YOQOcU2qM:&q=toy+story&tbnh=186&tbnw=124&usg=AI4_-kRx87Y8zXnFarhi_a6lfMtJeiXUBg&vet=12ahUKEwjersPc4MndAhUlpIsKHfINAosQ_B0wDXoECAYQCQ..i&docid=2bTAM2P4nI_n8M&itg=1&client=opera&sa=X&ved=2ahUKEwjersPc4MndAhUlpIsKHfINAosQ_B0wDXoECAYQCQ",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")



avatar = media.Movie("Avatar",
                        " A marine on an alien planet ",
                        "https://www.google.com/imgres?imgurl=http://www.gstatic.com/tv/thumb/v22vodart/3542039/p3542039_v_v8_ac.jpg&imgrefurl=http://google.com/search?tbm%3Disch%26q%3DAvatar&h=1440&w=960&tbnid=EjtSrMTdwp5H1M:&q=Avatar&tbnh=186&tbnw=124&usg=AI4_-kQTKJPYEj0eisuHKIHAZu-h_4h_kQ&vet=12ahUKEwjQw6jA4sndAhWt-ioKHQKJAfYQ_B0wIHoECAYQCQ..i&docid=UHUPOmPGfyBCqM&itg=1&client=opera&sa=X&ved=2ahUKEwjQw6jA4sndAhWt-ioKHQKJAfYQ_B0wIHoECAYQCQ",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")




gone_girl = media.Movie("Gone Girl",
                        " A Damon dengerous girl ",
                        "https://www.google.com/imgres?imgurl=http://www.gstatic.com/tv/thumb/v22vodart/10556843/p10556843_v_v8_ab.jpg&imgrefurl=http://google.com/search?tbm%3Disch%26q%3DGone%2BGirl&h=1440&w=960&tbnid=fPwyg75EHKTtnM:&q=gone+girl+movie&tbnh=186&tbnw=124&usg=AFrqEzdJkIb5l1i-2LSKZvK3YSraYEu8yg&vet=12ahUKEwj3jrqg7MndAhUrB8AKHQsYBOAQ_B0wFHoECAcQCQ..i&docid=L8crJVNYac0_dM&itg=1&client=opera&sa=X&ved=2ahUKEwj3jrqg7MndAhUrB8AKHQsYBOAQ_B0wFHoECAcQCQ",
                        "https://www.youtube.com/watch?v=2-_-1nJf8Vg")

#############################

harry_potter = media.Movie("Harry Potter",
                        " Magic Movie",
                        "https://www.google.com/search?q=harry+potter&client=opera&hs=oDO&tbm=isch&source=iu&ictx=1&fir=CzldG-iQu1QE5M%253A%252CEWCoypMAaaNCCM%252C_&usg=AFrqEzcCdW_56GT26-tsHZfvqdSaswn0Ew&sa=X&ved=2ahUKEwi4xoii78ndAhWCTcAKHSGpC7wQ_h0wIXoECAUQCQ#imgrc=a9rVT4l1WetvCM:",
                        "https://www.youtube.com/watch?v=eKSB0gXl9dw")



titanic = media.Movie("Titanic",
                        " Romantic love movie ",
                        "https://www.google.com/imgres?imgurl=http://www.gstatic.com/tv/thumb/v22vodart/20056/p20056_v_v8_ba.jpg&imgrefurl=http://google.com/search?tbm%3Disch%26q%3DTitanic&h=1440&w=960&tbnid=NlRWHyjZ016azM:&q=titanic&tbnh=186&tbnw=124&usg=AFrqEzcL0en0aHGB7dd6bpPpceKFkIdGUw&vet=12ahUKEwi6n5H-78ndAhVSgVwKHXbMBxYQ_B0wHnoECAUQCQ..i&docid=-wYqjwan1U0DYM&itg=1&client=opera&sa=X&ved=2ahUKEwi6n5H-78ndAhVSgVwKHXbMBxYQ_B0wHnoECAUQCQ",
                        "https://www.youtube.com/watch?v=2-_-1nJf8Vg")



hunger_games = media.Movie("Gone Girl",
                        " A Damon dengerous girl ",
                        "https://www.google.com/imgres?imgurl=http://www.gstatic.com/tv/thumb/v22vodart/10556843/p10556843_v_v8_ab.jpg&imgrefurl=http://google.com/search?tbm%3Disch%26q%3DGone%2BGirl&h=1440&w=960&tbnid=fPwyg75EHKTtnM:&q=gone+girl+movie&tbnh=186&tbnw=124&usg=AFrqEzdJkIb5l1i-2LSKZvK3YSraYEu8yg&vet=12ahUKEwj3jrqg7MndAhUrB8AKHQsYBOAQ_B0wFHoECAcQCQ..i&docid=L8crJVNYac0_dM&itg=1&client=opera&sa=X&ved=2ahUKEwj3jrqg7MndAhUrB8AKHQsYBOAQ_B0wFHoECAcQCQ",
                        "https://www.youtube.com/watch?v=2-_-1nJf8Vg")
movies=[toy_story,avatar,gone_girl,harry_potter,titanic,hunger_games ]
fresh_tomatoes.open_movies_page(movies)
