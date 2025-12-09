module Utilities where

import Data.Char (ord)
import Data.List.Split (splitOn)

parseInts :: String -> String -> [Int]
parseInts sep = map read . splitOn sep

ctoi :: Char -> Int
ctoi = subtract (ord '0') . ord
