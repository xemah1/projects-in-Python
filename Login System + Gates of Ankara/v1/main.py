import register
import list
import delete
import login

end = True
while end :
    print("register|login|userlist|delete|end")
    input = input().lower()
    if input[0] == "r" :
        register.main()
    elif input[0] == "l" :
        login.main()
    elif input[0] == "u" :
        list.main()    
    elif input[0] == "d" :
        delete.main()
    else :
        end = False
        print("Process terminated.")
        print('-'*50)
    del input

#sqlite3 viewer https://inloop.github.io/sqlite-viewer/