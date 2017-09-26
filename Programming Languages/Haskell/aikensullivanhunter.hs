

-- Ashley Aiken
-- Daryl Sullivan 
-- Becca Hunter


-- Sum all of the numbers in a list
recursive_sum [] = 0
recursive_sum (x:xs) = x + recursive_sum xs 

-- Sum all of the even numbers in a list
recursive_even [] = 0
recursive_even (x:xs) = if even x then x + recursive_even xs else 0 + recursive_even xs

-- Sum all of odd numbers in a list
recursive_odd [] = 0
recursive_odd (x:xs) = if odd x then x + recursive_odd xs else 0 + recursive_odd xs

-- Print hello and the persons name 
main = do
    putStrLn "What is your name?"
    name <- getLine
    print ("Hello " ++ name ++ "! Enjoy using our list functions!")










