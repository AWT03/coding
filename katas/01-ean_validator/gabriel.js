function validateEAN(eanCode) {
  let checksum = 0;
  for (let i=0; i<eanCode.length-1; i++){
    checksum += Number(eanCode[i]);
    if (i%2!=0){
      checksum += Number(eanCode[i])*2;
    }
  }
  checksum = (10 - (checksum % 10)).toString();
  return eanCode[eanCode.length-1] == checksum[checksum.length-1]
}

