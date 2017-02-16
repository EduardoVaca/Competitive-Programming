import Foundation

// number of elements
let n = Int(readLine()!)!

for _ in 0..<n {
  // read array and map the elements to integer
  let arr = readLine()!.components(separatedBy: " ").map{ Int($0)! }
  print(Int(floor(sqrt(Double(arr.last!))) - ceil(sqrt(Double(arr.first!))) + 1))
}
