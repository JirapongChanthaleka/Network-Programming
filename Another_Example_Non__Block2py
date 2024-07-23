while inputs:
    logging.info('Non Blocking - Waiting...')
    readable, writable, exceptional = select.select(inputs, outputs, inputs,0.5)
    
    print(readable)
    print(writable)
    print(exceptional)

    for s in writable:
        logging.info('Non Blocking - sending...')
        data = s.send(b'hello\r\n')
        logging.info('Non Blocking - sent : {data}...')
        outputs.remove(s)

    for s in readable:
        logging.info('Non Blocking - reading...')
        data = s.recv(1024)
        logging.info(f'Non Blocking - data: {len(data)}')
        logging.info(f'Non Blocking - closeing...')
        s.close()
        inputs.remove(s)
        break

    for s in exceptional:
        logginh.info(f'Non Blocking - error')
        inputs.remove(s)
        outputs.remove(s)
        break

def main():
    create_nonblocking_socket('voidrealms.com',80)

if __name__ == '__main__':
    main()