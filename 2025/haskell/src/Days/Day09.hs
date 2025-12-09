module Days.Day09 where

import Data.List.Split

dupe :: a -> (a, a)
dupe x = (x, x)

listToPair :: [a] -> (a, a)
listToPair [x, y] = (x, y)
listToPair _ = undefined

lineToPoint :: String -> (Int, Int)
lineToPoint = listToPair . map read . splitOn ","

area :: (Int, Int) -> (Int, Int) -> Int
area (x1, y1) (x2, y2) = abs (x1 - x2 + 1) * abs (y1 - y2 + 1)

liftA2WithSelf :: (Applicative f) => (a -> a -> b) -> f a -> f b
liftA2WithSelf f xs = liftA2 f xs xs

part1 :: String -> String
part1 = show . maximum . liftA2WithSelf area . map lineToPoint . lines
