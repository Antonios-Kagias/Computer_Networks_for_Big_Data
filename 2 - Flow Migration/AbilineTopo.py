from mininet.topo import Topo
class AbilineTopo(Topo):
    
    def __init__( self ):
        
        Topo.__init__( self )
        
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')    
        s10 = self.addSwitch('s10')
        s11 = self.addSwitch('s11')
        
        self.addLink(s1, h1, delay='3ms')
        self.addLink(s1, s2, delay='3ms')
        self.addLink(s1, s3, delay='3ms')
        self.addLink(s2, h2, delay='3ms')
        self.addLink(s2, s3, delay='3ms')
        self.addLink(s2, s4, delay='3ms')
        self.addLink(s3, h3, delay='3ms')
        self.addLink(s3, s6, delay='3ms')
        self.addLink(s4, h4, delay='3ms')
        self.addLink(s4, s5, delay='3ms')
        self.addLink(s5, h5, delay='3ms')
        self.addLink(s5, s6, delay='3ms')
        self.addLink(s5, s7, delay='3ms')
        self.addLink(s6, h6, delay='3ms')
        self.addLink(s6, s8, delay='3ms')
        self.addLink(s7, h7, delay='3ms')
        self.addLink(s7, s8, delay='3ms')
        self.addLink(s7, s10, delay='3ms')
        self.addLink(s8, h8, delay='3ms')
        self.addLink(s8, s9, delay='3ms')
        self.addLink(s9, h9, delay='3ms')
        self.addLink(s9, s11, delay='3ms')
        self.addLink(s10, h10, delay='3ms')
        self.addLink(s10, s11, delay='3ms')
        self.addLink(s11, h11, delay='3ms')




topos = { 'abilinetopo': ( lambda: AbilineTopo() ) }      