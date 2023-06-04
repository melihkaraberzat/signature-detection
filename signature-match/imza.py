import cv2
from skimage.metrics import structural_similarity as ssim #structure similarity index measure



def eslestirme(firstPath, secondPath):
    
    img1 = cv2.imread(firstPath)
    img2 = cv2.imread(secondPath)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) # gürültü azaltmak için gri 
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))

    cv2.imshow("İlk", img1)
    cv2.imshow("İkinci", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    benzerlikDegeri = "{:.2f}".format(ssim(img1, img2)*100) # çok küsüratlı bir değer döndürdüğü için 
                                                            # yüzdesel formatta elde etmek için formatladık.
    return float(benzerlikDegeri)




