module Days.Day06 where

import Control.Arrow ((***))
import Data.List (transpose)
import Data.Tuple (swap)

eval :: String -> [Int] -> Int
eval "+" = sum
eval "*" = product
eval _ = undefined

pivotRead :: String -> [[Int]]
pivotRead = transpose . fmap (fmap read . words) . lines

part1 :: String -> String
part1 = show . sum . uncurry (zipWith eval) . swap . (pivotRead *** words) . break (== '*')
