import Foundation

var result = 0
var counter = 1
var current3 = 0
var current5 = 0

repeat {
  current5 = 5 * counter
  if current5 < 20 {
    result += current5
  }
  current3 = 3 * counter
  if current3 < 20 && current3 % 5 != 0 {
    result += current3
  }
  counter += 1
} while current5 < 20 || current3 < 20

print(result)
