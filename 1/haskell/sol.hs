import System.IO
import Control.Monad

readInt :: String -> Int
readInt = read

main = do
  contents <- readFile "../input.txt"
  let nums = map readInt . words $ contents
  let part1 = product ([[x,y]| x <- nums, y  <- nums, x + y == 2020] !! 0)
  let part2 = product ([[x,y,z]| x <- nums, y  <- nums, z <- nums, x + y + z == 2020] !! 0)
  print $ "Part 1: " ++ (show part1)
  print $ "Part 2: " ++ (show part2)
