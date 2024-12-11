
#Aralarındaki mesafe hesaplamak istediğimiz noktalar.
points = [(5, 4), (3, 7), (12, 5), (4, -12), (22, 37), (3, -4), (7, 32)]

distances = [] # Hesaplanan mesafeleri saklayacağımız liste.

def euclideanDistance(point1, point2):
    #Öklid Hesabı
    return (point1, point2, (((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2)) ** .5) #Hesaplanan noktalar ve hesaplanan değer.

#Her bir nokta için diğer tüm noktalar arası mesafe hesaplayacak döngümüz.
for point1 in points:
    for point2 in points:
        distances.append(euclideanDistance(point1, point2)) if point1 != point2 else None # Hesaplanan noktaları ve hesaplanan değeri listemize ekliyoruz.

min_distance = min(distances, key = lambda x: x[2]) # 3. Eleman değerlendirilerek minimum mesafe değeri alınır.

print(f"En küçük mesafe {min_distance[0]} ile {min_distance[1]} arası {min_distance[2]}.") #Çıktımız